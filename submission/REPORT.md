# Báo cáo Day 08 — 2A202603178 - Nguyễn Cao Ngọc Đức

Lớp: L2 · Email: 26ai.ducncn@vinuni.edu.vn

> Một file duy nhất cho cả bài (đã gộp recipe, QC và ghi chú cá nhân). Mọi con số kèm **mẫu số** và nguồn (file nào). Viết bằng lời của bạn.

## 1. Model và recipe (Part 2–3)

| Lớp | Model + cỡ | Ngưỡng | Vì sao (dẫn `run_id` trong `model_log.csv`) |
|---|---|---|---|
| person / bicycle / motorbike / car / bus / truck | <<YOLO26m>> | <<theo lớp, từ threshold_sweep>> | <<>> |
| three_wheeler | <<YOLOE-26s, prompt: ...>> | <<>> | <<>> |

- Lệnh `merge_prelabels.py` đã dùng (dán nguyên): <<>>
- **Phiên bản SAM bạn chọn** (SAM 1 / 2.1 / 3) và lý do: <<chất lượng mask, tốc độ, RAM, quyền truy cập>>
- Lỗi nào **không sửa được bằng đổi ngưỡng** (ví dụ tuk-tuk bị gọi `car`)? Sửa thế nào? <<>>
- Box **điểm cao mà sai** hoặc **điểm thấp mà đúng** (ảnh nào): <<>>
- Giới hạn: chọn ngưỡng trên chính gold (4 ảnh) nên số đo máy trên gold là lạc quan: <<>>

<!-- student-model-observations -->
### Quan sát tour đã nhận từ học viên

Nguồn nguyên bản và bản sắp xếp: [observations](observations/model_observations_organized.md). Các mục dưới đây là quan sát học viên, không phải xác nhận đã sửa batch.

- r01: ghi nhận nhầm xích lô/tuk-tuk thành motorbike, bicycle hoặc truck ở img_007, img_011, img_032; box trùng ở img_015 và img_030; thiếu tuk-tuk ở img_002.
- r02: học viên nhận xét các phần còn lại đúng nhưng các ca img_002, img_011, img_032 vẫn sai như r01; minivan img_016 được học viên xác nhận giữ nhãn car.
- r03: thiếu three_wheeler ở img_032, giữa hai box có điểm0.92 và0.27. Học viên đã chốt tuk-tuk thuộc three_wheeler; img_002 còn cần kiểm vị trí/độ đầy đủ của box.
- r04: ba tuk-tuk ở img_004 bị gọi car; img_013 thiếu person và có box car lệch. Minivan giữ car theo xác nhận của học viên. Chưa có nhận xét biên mask; xe ở xa còn cần đối chiếu ngưỡng kích thước/độ che.

Các hướng sửa do học viên đề xuất đã đưa vào model_log.csv. Chưa có quyết định cuối cùng chọn model/ngưỡng hoặc kết luận chất lượng mask từ học viên.

## 2. AI error profile (từ `qc/review_stats.md`)

| Trạng thái | Số | Tỉ lệ | Mẫu số |
|---|---|---|---|
| accepted | <<>> | <<>> | <<box máy>> |
| edited | <<>> | <<>> | <<>> |
| deleted | <<>> | <<>> | <<>> |
| added | <<>> | <<>> | <<đối tượng sau duyệt>> |

- Lớp nào máy tệ nhất? Vì sao (dẫn ảnh)? <<>>
- So với gold: precision / recall của **máy** <<>> (mẫu số: <<đối tượng gold>>)

## 3. Thiên kiến tự động hóa và ảnh bẫy

- Bắt bẫy: <<.../12>>; loại nào lọt: <<>>; vì sao (bạn đã bỏ bước nào của checklist)? <<>>
- Accepted cao mà bắt bẫy thấp (hoặc ngược lại) nói gì về cách bạn duyệt? <<>>

## 4. Máy có đáng dùng không?

- Thời gian (từ `time_log.csv`): gán tay <<... phút/ảnh>> vs duyệt <<... phút/ảnh>>. Thiên lệch (bạn gán gold trước nên đã quen cảnh): <<>>
- Kết luận: <<có / không / chỉ cho lớp nào>>, dựa trên <<số liệu>>
- **Ba quy tắc giảm thiên kiến của bạn** (mỗi quy tắc kiểm tra được bằng số hoặc việc làm):
  1. <<>>
  2. <<>>
  3. <<>>

## 5. Mask SAM cho 3 vật (Part 5)

| Ảnh | SAM (phiên bản) | Số click | Mask gồm người lái / hàng hoá? | Lỗi quan sát | File trong `masks/` |
|---|---|---|---|---|---|
| <<img_0xx>> | <<>> | <<>> | <<>> | <<>> | <<>> |

- Đối chiếu guideline mục 4.2: quy tắc nào giúp, quy tắc nào thiếu? <<>>
- *(Tuỳ chọn)* Interactor SAM trong CVAT: làm được / không (lỗi gì, đã thử gì); khác gì offline: <<>>

## 6. Calibration (Part 6)

- Số quyết định: <<>> (`calibration_decisions.csv`); quan trọng nhất (dẫn `CAL-xx`): <<>>
- Quy tắc mới đã vào `guideline_v1.1_calibrated.md`: <<>>
- Nguyên nhân gốc: <<guideline mơ hồ / chưa nắm quy tắc / máy>>

## 7. QC và quyết định (Part 6)

- Mẫu: <<n>> ảnh (<<m>> ảnh `can_review` + <<k>> ngẫu nhiên, seed 42); người kiểm: bạn (**hạn chế**: bạn vừa là người duyệt).
- Lỗi theo **đối tượng**: <<.../... = ...%>> · theo **ảnh**: <<.../... = ...%>> (ngưỡng Release ≤ 2%)
- Top lỗi (trong: bỏ sót, thừa, sai lớp, sai vị trí/kích thước, sai thuộc tính, sai mask) + một ảnh ví dụ mỗi loại: <<>>
- **Giới hạn mẫu nhỏ** (cận trên 95% trong `qc_report_auto.md`): <<>>
- Script kiểm được / không kiểm được (ví dụ ôm sát, cùng bỏ sót với máy, theo checklist thật): <<>>

**Quyết định: <<Release / Hold / Rework>>**, ngày <<YYYY-MM-DD>>. Lý do (đi theo Hold → Rework → Release): <<>>
Nếu Rework / Hold, việc cần làm tiếp: <<>>

## 8. Ghi chú cá nhân

- **Dùng AI để làm bài:** Codex hỗ trợ môi trường, lệnh chạy model local, xuất/kiểm schema nhãn, chuẩn bị giao diện xem ảnh và bấm giờ. Nhận xét model, review ảnh, quyết định calibration và kết luận báo cáo còn chờ học viên thực hiện/xác nhận.
- **Giới hạn tính độc lập của gold:** trước khi hoàn thành gán, học viên đã gửi screenshot hỏi chatbot về gương xe, box người/xe máy và ignore_region. Cần ghi nhận hỗ trợ này khi diễn giải số đo, không khẳng định gold hoàn toàn độc lập với AI. Trong luồng chạy đã lưu, gold được xuất và sửa theo kiểm tra kích thước trước khi chạy model lên gold; bản hash cuối được giữ ở labels/gold_provenance.json.
- Máy: Windows11, RTX4060Laptop8GB, RAM16GB; PyTorch2.10.0+cu128, Ultralytics8.4.214, CVAT2.74.1 tại localhost:8081. Venv tái sử dụng thư viện GPU hiện có; đã sửa đường dẫn .pth bị cũ sau đổi tên thư mục. Không cài thêm CVAT.
- Không dùng cache data/cache: r01–r06 là suy luận thật trên GPU local; số kỹ thuật lưu ở model_log.csv và work/runs.csv. Các ô nhận xét còn trống chưa được coi là đã quan sát.
- Chưa sửa thuật toán script đề. Thêm scripts/prepare_model_tour.py để tạo trang xem ảnh/nhận xét local và đồng hồ review; launcher đặt YOLO_CONFIG_DIR riêng. File đề, taxonomy.rules, data/split.csv và ảnh nguồn giữ nguyên.
- Một điều bạn làm khác lần sau: <<>>
