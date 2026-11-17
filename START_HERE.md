# Bắt đầu Day08 trên máy này

Nguyễn Cao Ngọc Đức — 2A202603178 — L2 — 26ai.ducncn@vinuni.edu.vn

## Trạng thái

- Đã đọc GUIDE.md, RULES.md, SUBMISSION.md, rubric và label contract v1.0.
- Môi trường `.venv` dùng lại PyTorch CUDA hiện có; không cài thêm bản torch hoặc CVAT.
- `check_env.py` đạt tất cả mục bắt buộc, GPU RTX 4060 và CVAT 8081 hoạt động.
- Model: YOLO26m (mới tải, SHA256 xác nhận theo release chính thức), YOLOE-26s-seg, SAM2.1-base. Ba file YOLOE/SAM/text encoder dùng hard link tới kho có sẵn, không nhân đôi dung lượng.
- SAM3 vẫn giữ ở F:\Projects\SAM3. Đây là phần tùy chọn; bài chính dùng SAM2 cho click-mask. Cảnh báo token Windows trong check_env không chặn bài chính, không có nghĩa quyền HF đã bị mất.
- Các bản YOLO26n/s, MobileSAM, cache cài đặt dở đã được dọn ở đợt trước; nhật ký tại F:\Projects\day08\logs\cleanup-*.json. YOLO11m/EfficientSAM3/SegFormer dùng cho bài cũ vẫn giữ để tái lập kết quả.
- Chưa chạy suy luận hay đọc nội dung 4 ảnh gold. Chưa có metric, thời gian gán tay hoặc kết luận Release.

## Việc cần làm ngay: gán tay gold

Mở [job gold trong CVAT](http://localhost:8081/tasks/24/jobs/23), đăng nhập tài khoản ducncn đang dùng.
Task chỉ có **img_001.jpg, img_012.jpg, img_020.jpg, img_036.jpg**. Gán cả 4, không dùng AI Tools/pre-label. Bấm giờ thực tế từ khi bắt đầu đến khi xong; không lấy thời gian setup làm thời gian gán.

Theo `guideline/guideline_v1.0_label_contract.md`:
- Nhãn: person, bicycle, motorbike, car, bus, truck, three_wheeler, ignore_region.
- Vẽ box sát phần nhìn thấy, không đoán phần bị che; người ngồi xe là box person riêng.
- Bán tải thuộc car; tuk-tuk/xích lô/ba gác thuộc three_wheeler. Không dùng quy tắc Day07 thay cho Day08.
- Bỏ vật nhỏ hơn điều kiện ở mục 4 và vật còn nhìn thấy dưới 20%; không gán tượng, ảnh quảng cáo hoặc phản chiếu.
- Nhãn vẽ tay để conf trống. Tick can_review khi chưa chắc quy tắc và ghi ca đó để calibration.

Lưu CVAT, xuất **COCO 1.0**, không kèm ảnh. Đặt JSON nhãn tại `submission/labels/gold_manual.json` (giải nén file xuất nếu cần). Khi xong báo lại thời gian gán thực tế và các ca chưa chắc; lúc đó mới chạy các bước máy.

## Lệnh kiểm tra

Mở PowerShell trong thư mục repo:

```powershell
.\run-day08.ps1 check
```

Không cần kích hoạt venv thủ công. Launcher `script` chạy đúng các script chính thức và chặn prelabel trước khi có file gold:

```powershell
.\run-day08.ps1 script prelabel.py --model yolo26 --size m --split pilot --conf 0.25 --out work/prelabel/t_y26
```

## Các bước tiếp theo sau gold

1. Validate và giữ bản gold trước lần chạy model đầu tiên; commit Part 1.
2. Chạy ít nhất 4 lần theo GUIDE: YOLO26m hai ngưỡng, YOLOE three_wheeler, YOLO26 + SAM2. Xem output rồi điền model_log bằng quan sát thực tế.
3. Sweep ngưỡng trên gold; merge pre-label; inject 12 bẫy với seed 2A202603178. Không mở traps_key trước khi xuất bản batch đã duyệt.
4. Import đúng 24 ảnh batch vào CVAT, duyệt và đo thời gian thật; xuất batch_reviewed.json rồi tính review_stats.
5. Tạo ít nhất 3 ví dụ SAM click-mask, chốt ít nhất 3 ca calibration, QC mẫu theo hướng dẫn, chạy kiểm tra bài nộp và hoàn thiện báo cáo bằng kết quả thật.
6. Đổi tên repo theo SUBMISSION.md trước khi chốt link; không coi repo hiện tại là bài đã hoàn thành.

Không cần bật Nuclio để hoàn thành luồng offline bắt buộc của bài này.
