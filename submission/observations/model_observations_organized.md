# Nhận xét tour model — bản sắp xếp lại

Nguồn học viên: `day08-model-observations.original.json`, ghi lúc 2026-11-19T04:42:38.706Z. SHA256: `d788dfc2f3acc43e39c039725954cad3e5d9db832a58b0b87b99854f2a6c564e`.

Chỉ sắp xếp và biên tập ý đã gửi. Không có lần xem ảnh bổ sung nào được xác nhận. Các lỗi dưới đây là quan sát của học viên, chưa phải nhãn batch đã sửa. Dấu chấm và dòng dang dở không được tính là nhận xét.

## r01

**Điểm làm đúng:** Chưa có nhận xét riêng về điểm làm đúng trong nội dung đã gửi.

**Lỗi quan sát:** img_002: xe bên phải bị gọi truck thay vì car; bỏ sót xe xanh lá ở giữa (học viên xác định tuk-tuk). img_007: xích lô bên trái vỉa hè bị gọi motorbike. img_011: tuk-tuk bên trái bị gọi truck. img_015: một bicycle có hai box. img_019: box truck conf0.45 cần đổi car theo quan sát học viên. img_030: car bên phải có hai box. img_032: các xích lô bị gọi bicycle. img_016: học viên gọi xe car conf0.73 là van; chưa xác minh loại van theo label contract.

**Hướng xử lý / trạng thái:** Theo đề xuất của học viên: sửa các lớp sai, thêm three_wheeler bị sót và bỏ box trùng cùng vật. Ca van img_016 để xác minh; chưa đổi car chỉ vì tên gọi van.

## r02

**Điểm làm đúng:** Học viên nhận xét các phần còn lại được gán đúng; nhận xét này không kèm danh sách từng box.

**Lỗi quan sát:** Học viên ghi các ca img_032, img_011, img_002 vẫn sai như r01. Ca img_016 được nhắc lại như r01 nhưng loại van chưa rõ.

**Hướng xử lý / trạng thái:** Giữ các lỗi được học viên nhắc lại để sửa khi review; chưa có lựa chọn model/ngưỡng cuối cùng từ học viên.

## r03

**Điểm làm đúng:** Chưa có nhận xét riêng về điểm làm đúng trong nội dung đã gửi.

**Lỗi quan sát:** img_032: học viên thấy thiếu một three_wheeler giữa hai xe có conf0.92 và0.27. img_002: ghi chú "gán sai nhãn three wheeler, xe xanh lá cây ở giữa là tuk_tuk" còn mơ hồ: tuk-tuk đã thuộc three_wheeler; cần làm rõ bỏ sót hay box đặt nhầm vật.

**Hướng xử lý / trạng thái:** Theo quan sát học viên: bổ sung three_wheeler còn thiếu ở img_032. Chờ xác minh ca img_002, không tạo lớp tuk_tuk riêng.

## r04

**Điểm làm đúng:** Chưa có nhận xét về chất lượng biên mask SAM trong nội dung đã gửi.

**Lỗi quan sát:** img_004: ba đối tượng gán car được học viên xác định là tuk-tuk. img_013: thiếu person ngồi phía trước xe; box car lệch; học viên đề nghị bỏ xe phía bên phải ở xa, chưa ghi chiều cao box/độ che; một xe khác được gọi van nhưng chưa rõ loại.

**Hướng xử lý / trạng thái:** Theo đề xuất học viên: đổi ba tuk-tuk img_004 sang three_wheeler, thêm person và chỉnh box lệch img_013. Ca xe xa cần đối chiếu cao20px/độ che; ca van chờ xác minh. Chưa chốt đánh giá mask SAM.

## Những điểm cần xác minh

- img_002/r03: tuk-tuk thuộc three_wheeler; cần xác nhận box thiếu hay box đặt nhầm vật.
- img_016/r01–r02 và img_013/r04: guideline xếp minivan vào car; không có lớp van. Chưa có thông tin đủ để đổi sang truck/bus.
- img_013/r04: ở xa không tự đủ lý do bỏ nhãn; đối chiếu cao<20px hoặc còn nhìn thấy<20% theo guideline.
- r04: còn thiếu quan sát mask bám biên, có gom người lái/hàng hóa/nền hay không.
- Nhận xét tour dùng ảnh pilot và hai ảnh demo; không thay cho việc sửa và lưu 24 ảnh batch trong CVAT.
