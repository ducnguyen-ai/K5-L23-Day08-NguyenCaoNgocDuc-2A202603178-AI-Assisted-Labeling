# Day08 — Tiếp tục sau gold

Nguyễn Cao Ngọc Đức — 2A202603178 — L2

## Đã hoàn thành có bằng chứng

- Gold: img_001, img_012, img_020, img_036; học viên xác nhận đã sửa các box nhỏ, xuất lại từ task24/job23. Validate: 4 ảnh, 72 đối tượng, OK. Lịch sử hash: submission/labels/gold_provenance.json.
- Thời gian gold do học viên cung cấp: 60 phút/4 ảnh. Chưa có thời gian review batch.
- Chạy local RTX4060: YOLO26m hai ngưỡng, YOLOE three_wheeler, YOLO26m + SAM2.1-base. Bốn lượt tour r01–r04 có ảnh minh họa; đã nhận JSON nhận xét học viên và sắp xếp vào submission/model_log.csv. Đã chốt tuk-tuk → three_wheeler, minivan → car. Còn kiểm vị trí/độ đầy đủ box img_002/r03 và đánh giá biên mask.
- Chạy thêm YOLO26m và YOLOE trên 36 ảnh ở conf0.05; threshold_sweep trên bản gold đã sửa. Chuỗi ngưỡng: motorbike=0.2,three_wheeler=0.15; mặc định0.3. Không phải mọi lớp đều đạt recall90%.
- Merge YOLOE trước YOLO26, IoU0.6, 28 ảnh batch+gold. Chèn 12 bẫy theo MSHV2A202603178 bằng script đề. Chưa mở đáp án.
- CVAT hiện có: [job batch review](http://localhost:8081/tasks/26/jobs/25), 24 ảnh, 567 box nhập từ pre_traps_import.coco.json. Không ghi đè job gold hay bài cũ.

## Bạn làm ngay

Hướng dẫn cụ thể thao tác review: [docs/DAY08_REVIEW_HUONG_DAN.md](docs/DAY08_REVIEW_HUONG_DAN.md).

1. Nhận xét tour đã lưu tại submission/observations/. Xem các ca cần xác minh trong bản sắp xếp; chưa coi các ô chỉ có dấu chấm là quyết định.
2. Mở `work/model_tour/review-timer.html`. Bấm Bắt đầu khi bắt đầu review; Tạm dừng khi nghỉ. Mở job batch bằng link trong trang.
3. Mỗi ảnh: ẩn nhãn → quét ảnh → hiện nhãn → tìm bỏ sót → xóa thừa → sửa lớp → chỉnh box. Người và phương tiện có box riêng; box sát phần nhìn thấy. Nhãn vẽ tay conf trống; giữ conf của máy. can_review dành cho ca chưa chắc quy tắc.
4. Sau mỗi khoảng 10 ảnh, nghỉ và tạm dừng đồng hồ. Khi xong đủ 24 ảnh: Save trong CVAT, dừng/tải day08-batch-time.json và báo đã xong. Có thể gửi file thời gian; tôi sẽ xuất nhãn từ CVAT.
5. Không mở submission/prelabel/traps_key.json trước khi xuất batch_reviewed.json. Không dùng lại gold để làm batch.

## Các phần còn lại

- Sau review: validate, review_stats và tỷ lệ bắt bẫy; không coi pre-label là nhãn đã duyệt.
- Ba ví dụ SAM click-mask: bạn chọn vật và nhận xét mask (có ôm người/hàng hóa không).
- Ít nhất ba quyết định calibration, gồm lỗi máy và câu hỏi quy tắc; guidelinev1.1 phải khớp quyết định của bạn.
- QC mẫu5ảnh, báo cáo và quyết định theo số liệu; chạy check_submission, push kết quả. Bài chưa đủ điều kiện chốt nộp hoàn chỉnh.

## Tái lập

```powershell
.\run-day08.ps1 check
.\run-day08.ps1 script prepare_model_tour.py
```

Lệnh merge đã dùng:

```powershell
.\run-day08.ps1 script merge_prelabels.py work/prelabel/yoloe_all/pre.coco.json work/prelabel/y26_all/pre.coco.json --thr "motorbike=0.2,three_wheeler=0.15" --conf .3 --iou .6 --split "batch,gold" --out work/prelabel/merged_review/pre.coco.json
```

Không chạy lại inject_traps hoặc nhập đè task26 sau khi bắt đầu review. Giữ tên repo có NguyenCaoNgocDuc trước MSHV theo yêu cầu cá nhân.

## Kiến thức cần nắm

Gold đo chất lượng máy; batch có bẫy đo cả khả năng review. Confidence không phải xác suất đúng. Đổi ngưỡng cân bằng precision/recall nhưng không chữa được sai lớp hoặc vật hoàn toàn không tìm thấy. Chọn và chấm trên cùng4ảnh gold làm số đo lạc quan. Accepted cao không chứng minh không bỏ sót; cần xem added, recall và bẫy. Mask phải được kiểm theo biên và label contract. QC mẫu nhỏ không bảo đảm toàn bộ lô sạch.

## Bonus

RUBRIC cho tối đa +5 từ docs/ADVANCED.md. Hiện chưa xác nhận hoàn thành bonus. Có thể chọn pilot độc lập, mask8ảnh, tích hợp CVAT hoặc gán lại mù; mỗi lựa chọn cần quan sát/nhãn và bằng chứng thật. Không cài thêm model chỉ để có tên trong log. Chốt bài cốt lõi trước.
