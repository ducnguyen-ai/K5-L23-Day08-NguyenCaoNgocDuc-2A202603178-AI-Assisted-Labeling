# Bạn cần làm gì khi review 24 ảnh?

Review là **sửa trực tiếp nhãn máy trong CVAT**, đến khi từng ảnh đúng guideline. Ghi nhận xét trên trang tour model là Part2; sửa24ảnh là Part4. Không cần vẽ lại mọi box: box đúng thì giữ nguyên.

## Mở đúng chỗ và bấm giờ

- [Job batch: task26/job25](http://localhost:8081/tasks/26/jobs/25): 24 ảnh batch, đã có pre-label. Đừng sửa vào task gold24/job23 cho bước này.
- Mở `work/model_tour/review-timer.html`: bấm Bắt đầu khi thực sự bắt đầu review; Tạm dừng khi nghỉ. Xem hướng dẫn/setup không tính vào thời gian sửa nhãn.

## Với mỗi ảnh

1. Dùng biểu tượng con mắt ở bảng Objects để ẩn toàn bộ nhãn. Nhìn ảnh khoảng15giây, tự tìm người và xe, cả vùng xa/mép ảnh. Rồi hiện nhãn lại.
2. **Bỏ sót:** vật đúng phạm vi, đủ lớn nhưng chưa có box → chọn công cụ Rectangle, chọn lớp và vẽ box mới.
3. **Thừa:** box không có vật hợp lệ → chọn đúng box rồi xóa. Nếu hai box cùng bọc một vật → giữ một box sát vật, xóa box trùng. Hai vật khác nhau chồng lên nhau vẫn có thể cần hai box.
4. **Sai lớp:** chọn box, đổi nhãn trong mục label của đối tượng ở bảng Objects. Ví dụ đã tự xác định là xích lô/tuk-tuk nhưng box đang ghi motorbike/car → đổi three_wheeler; không tạo lớp tuk_tuk.
5. **Box lỏng/lệch:** chọn box, kéo góc/cạnh cho sát phần nhìn thấy. Không kéo bao thêm phần bị khuất. Người trên xe và xe có hai box riêng.
6. Giữ nguyên conf của box máy; box vẽ mới conf trống. Không tự cho điểm. Nếu không chắc quy tắc, tick can_review và ghi lại tên ảnh, vật, câu hỏi.
7. Save rồi chuyển ảnh tiếp theo. Sau khoảng10ảnh, nghỉ3–5phút và tạm dừng đồng hồ.

## Quy tắc dễ nhầm

- Minivan thuộc car; không có lớp van. Cần phân biệt cụ thể với xe tải thùng hoặc minibus, đừng đổi chỉ theo tên gọi.
- Xa không đồng nghĩa bỏ. Box cao<20px thì không gán riêng; cụm≥5vật nhỏ sát nhau dùng ignore_region. Vật còn thấy<20% cũng không gán theo contract.
- Nhãn đúng nhưng conf thấp vẫn giữ; conf cao nhưng sai vẫn sửa.
- can_review dành cho câu hỏi quy tắc, không thay việc sửa một lỗi đã biết.
- Áp dụng cả24ảnh theo guideline; các nhận xét ở tour không phải danh sách đầy đủ lỗi của batch.

## Kết thúc

Save đủ24ảnh. Dừng đồng hồ, tải `day08-batch-time.json`, gửi lại và báo “đã review xong24ảnh”. Tôi sẽ xuất `batch_reviewed.json` từ CVAT rồi mới chạy đo accepted/edited/deleted/added và tỷ lệ bắt bẫy. Không mở `traps_key.json` trước khi xuất bản đã duyệt.

Không phải săn đúng12lỗi: ảnh có lỗi tự nhiên của model lẫn lỗi cài bẫy. Mục tiêu là làm nhãn đúng theo ảnh và guideline.

Nguồn: [label contract](../guideline/guideline_v1.0_label_contract.md), [checklist chính thức](REVIEW_CHECKLIST.md), [GUIDE Part4](../GUIDE.md).
