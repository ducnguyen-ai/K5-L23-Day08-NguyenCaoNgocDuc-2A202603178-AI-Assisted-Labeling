"""Prepare a local-only model tour and an explicit review stopwatch. No model inference."""
from pathlib import Path
import csv,json,html
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'work/runs.csv').open(encoding='utf-8-sig',newline='')))
fields=['run_id','part','model','params','split','n_boxes','sec_per_img','what_went_right','what_went_wrong','decision']
log=ROOT/'submission/model_log.csv'
existing={r['run_id']:r for r in csv.DictReader(log.open(encoding='utf-8-sig',newline=''))}
for r in rows:
 r['part']='2' if r['run_id'] in ['r01','r02','r03','r04'] else '3'
 for k in ['what_went_right','what_went_wrong','decision']:
  r[k]=existing.get(r['run_id'],{}).get(k,'')
with log.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
out=ROOT/'work/model_tour';out.mkdir(parents=True,exist_ok=True)
parts=[]
for r in rows[:4]:
 folder=ROOT/r['out'].replace('\\','/')
 imgs=sorted((folder/'viz').glob('*.jpg'))
 cards=''.join(f'<a href="../{p.relative_to(ROOT/"work").as_posix()}" target="_blank"><img loading="lazy" src="../{p.relative_to(ROOT/"work").as_posix()}"><span>{html.escape(p.name)}</span></a>' for p in imgs)
 inputs=''.join(f'<label>{label}<textarea data-run="{r["run_id"]}" data-field="{k}" placeholder="Ghi tên ảnh, vật và lỗi cụ thể; đây là quan sát của bạn."></textarea></label>' for k,label in [('what_went_right','Làm đúng gì?'),('what_went_wrong','Sai / bỏ sót gì?'),('decision','Bạn chọn / thay đổi gì và vì sao?')])
 parts.append(f'<section><h2>{r["run_id"]}: {html.escape(r["model"])}</h2><p>{r["n_boxes"]} box, {r["sec_per_img"]} giây/ảnh. <code>{html.escape(r["params"])}</code></p><div class="grid">{cards}</div>{inputs}</section>')
page='''<!doctype html><meta charset="utf-8"><title>Day08 — Quan sát model</title>
<style>body{font:17px system-ui;max-width:1100px;margin:30px auto;padding:20px;background:#f3f5fa;color:#17243b}section{background:white;padding:24px;margin:24px 0;border-radius:12px}.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}img{width:100%}a{color:#125294}label{display:block;margin:16px 0}textarea{display:block;width:98%;min-height:85px;font:inherit}button{padding:12px 22px;font:inherit;background:#174fa3;color:white;border:0;border-radius:7px}code{overflow-wrap:anywhere}span{display:block}</style>
<h1>Day08 — Xem và ghi nhận xét 4 lần chạy thật</h1><p>Trang chạy trên máy bạn, không gửi ảnh hoặc câu trả lời lên dịch vụ nào. Bấm ảnh để xem lớn. So sánh r01 với r02 trên cùng ảnh; ít box hơn chưa có nghĩa tốt hơn. r04 có mask nhưng vẫn cần tự đánh giá biên mask.</p><p>Hoàn thành nhận xét rồi tải JSON và gửi lại trong chat. Chưa điền sẽ không được coi là đã quan sát.</p>'''+''.join(parts)+'''
<button onclick="save()">Tải day08-model-observations.json</button><p id="msg"></p>
<script>
const key='day08-model-tour-v1',els=[...document.querySelectorAll('textarea')];
let stored=JSON.parse(localStorage.getItem(key)||'{}');
for(const e of els){const id=e.dataset.run+'.'+e.dataset.field;e.value=stored[id]||'';e.oninput=()=>{stored[id]=e.value;localStorage.setItem(key,JSON.stringify(stored));};}
function save(){if(els.some(e=>!e.value.trim())){document.getElementById('msg').textContent='Cần điền đủ 3 nhận xét cho mỗi lần chạy.';return;}
let runs={};for(const e of els){(runs[e.dataset.run]??={run_id:e.dataset.run})[e.dataset.field]=e.value.trim();}
let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify({recorded_at:new Date().toISOString(),observations:Object.values(runs)},null,2)],{type:'application/json'}));a.download='day08-model-observations.json';a.click();URL.revokeObjectURL(a.href);}
</script>'''
(out/'index.html').write_text(page,encoding='utf-8')
(out/'review-timer.html').write_text('''<!doctype html><meta charset="utf-8"><title>Day08 — Bấm giờ review</title><style>body{font:20px system-ui;max-width:780px;margin:60px auto;padding:24px}button{font:inherit;margin:8px;padding:12px}output{display:block;font-size:48px;margin:24px 0}</style><h1>Bấm giờ review 24 ảnh</h1><p>Chỉ bấm Bắt đầu khi bạn thực sự review. Tạm dừng khi nghỉ hoặc làm việc khác. Thời gian vẫn được lưu khi đóng/mở trang; hãy tạm dừng trước khi đóng nếu ngừng làm.</p><p><a href="http://localhost:8081/tasks/26/jobs/25" target="_blank">Mở job batch review trong CVAT</a></p><output id="clock"></output><button onclick="start()">Bắt đầu / tiếp tục</button><button onclick="pause()">Tạm dừng</button><button onclick="download()">Dừng và tải số đo</button><p>Ẩn nhãn và quét ảnh trước; rồi kiểm bỏ sót → thừa → sai lớp → box lỏng. Giữ conf máy; box tự vẽ để trống. Không mở đáp án bẫy.</p><script>
const key='day08-batch-timer-task26-v1';let state=JSON.parse(localStorage.getItem(key)||'{"elapsed_ms":0,"started_at":null,"sessions":[]}');function persist(){localStorage.setItem(key,JSON.stringify(state));}function elapsed(){return state.elapsed_ms+(state.started_at?Math.max(0,Date.now()-state.started_at):0);}function start(){if(!state.started_at){state.started_at=Date.now();persist();}}function pause(){if(state.started_at){const end=Date.now();state.sessions.push({start:new Date(state.started_at).toISOString(),end:new Date(end).toISOString()});state.elapsed_ms+=Math.max(0,end-state.started_at);state.started_at=null;persist();}}function download(){pause();if(state.elapsed_ms<=0)return;const data={step:'batch_review',task_id:26,images:24,minutes:state.elapsed_ms/60000,...state};const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(data,null,2)],{type:'application/json'}));a.download='day08-batch-time.json';a.click();URL.revokeObjectURL(a.href);}setInterval(()=>{document.getElementById('clock').textContent=(elapsed()/60000).toFixed(2)+' phút'+(state.started_at?' — đang chạy':' — tạm dừng');},250);
</script>''',encoding='utf-8')
print('Prepared',out/'index.html','and review-timer.html; preserved existing human observations.')
