# Nhận xét tour model — bản sắp xếp lại

Nguồn gốc: day08-model-observations.original.json. Xác nhận bổ sung: class_clarifications.json. Giữ nguyên file nhận xét gốc.

Học viên đã chốt: tuk-tuk thuộc three_wheeler; minivan thuộc car. Cả hai phù hợp guideline v1.0, không tạo nhãn mới. Đây là nhận xét và hướng sửa, chưa xác nhận đã sửa nhãn batch.

## r01

**Điểm làm đúng:** Theo xác nhận bổ sung của học viên: minivan img_016 giữ nhãn car; không tính việc gọi car cho minivan là lỗi.

**Lỗi quan sát:** img_002: xe bên phải bị gọi truck thay vì car; bỏ sót xe xanh lá ở giữa (học viên xác định tuk-tuk). img_007: xích lô bên trái vỉa hè bị gọi motorbike. img_011: tuk-tuk bên trái bị gọi truck. img_015: một bicycle có hai box. img_019: box truck conf0.45 cần đổi car theo quan sát học viên. img_030: car bên phải có hai box. img_032: các xích lô bị gọi bicycle.

**Hướng xử lý / trạng thái:** Theo đề xuất học viên: sửa các lớp sai, thêm three_wheeler bị sót và bỏ box trùng cùng vật. Tuk-tuk thuộc three_wheeler; minivan img_016 giữ car theo xác nhận bổ sung.

## r02

**Điểm làm đúng:** Học viên nhận xét các phần còn lại được gán đúng; nhận xét này không kèm danh sách từng box. Xác nhận bổ sung: minivan img_016 thuộc car, giữ nhãn car.

**Lỗi quan sát:** Học viên ghi các ca img_032, img_011, img_002 vẫn sai như r01. Loại ca minivan img_016 khỏi danh sách lỗi lớp vì minivan thuộc car.

**Hướng xử lý / trạng thái:** Giữ các lỗi được học viên nhắc lại để sửa khi review; chưa có lựa chọn model/ngưỡng cuối cùng từ học viên.

## r03

**Điểm làm đúng:** Chưa có nhận xét riêng về điểm làm đúng trong nội dung đã gửi.

**Lỗi quan sát:** img_032: học viên thấy thiếu một three_wheeler giữa hai xe có conf0.92 và0.27. img_002: học viên đã chốt tuk-tuk thuộc three_wheeler; mô tả ban đầu chưa cho biết rõ box bị thiếu hay đặt nhầm vật.

**Hướng xử lý / trạng thái:** Theo quan sát học viên: bổ sung three_wheeler còn thiếu ở img_032. Tuk-tuk dùng nhãn three_wheeler, không tạo lớp tuk_tuk. Vị trí/độ đầy đủ box img_002 còn cần kiểm khi review.

## r04

**Điểm làm đúng:** Theo xác nhận bổ sung: minivan thuộc car, giữ/gán car cho ca minivan đã nêu ở img_013. Chưa có nhận xét biên mask SAM.

**Lỗi quan sát:** img_004: ba đối tượng gán car được học viên xác định là tuk-tuk (thuộc three_wheeler). img_013: thiếu person ngồi phía trước xe; box car lệch; học viên đề nghị bỏ xe phía bên phải ở xa, chưa ghi chiều cao box/độ che. Minivan không tính là lỗi lớp car.

**Hướng xử lý / trạng thái:** Theo đề xuất học viên: đổi ba tuk-tuk img_004 sang three_wheeler, thêm person và chỉnh box lệch img_013; giữ minivan là car. Ca xe xa cần đối chiếu cao20px/độ che. Chưa chốt đánh giá mask SAM.

## Phần còn cần kiểm

- img_002/r03: lớp tuk-tuk đã rõ; còn cần kiểm box thiếu hay đặt nhầm vật.
- img_013/r04: đối chiếu cao<20px hoặc phần nhìn thấy<20% trước khi bỏ một xe ở xa.
- r04: còn thiếu quan sát mask bám biên, có gom người lái/hàng hóa/nền hay không.
- Nhận xét tour không thay cho sửa và lưu 24 ảnh batch trong CVAT.
