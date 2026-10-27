# Qikify BFCM: Mystery Box Drop

## Concept: "Bức tường 100 hộp"

Campaign có đúng **100 hộp**, nên key visual lấy chính con số này làm hình ảnh: một bức tường 10×10 hộp, đánh số từ 001 đến 100 như một đợt "drop" giới hạn. Hộp đã mở sáng lên theo màu tier, và **hộp của bạn** (màu đỏ cam, có dấu "?") đang được kéo ra khỏi tường, nghiêng như đang rung. Ý tưởng: cảm giác mở quà, thấy rõ số hộp còn lại, và còn cơ hội trúng lớn.

- **Qikify là chính**: logo Qikify nằm ở vị trí brand, headline và CTA nói về Qikify. Mysbox chỉ xuất hiện như dòng phụ "Unboxing by Mysbox".
- **BFCM**: nền đen ấm (Black Friday), dải băng đỏ cam "Black Friday / Cyber Monday / 100 boxes" làm họa tiết lặp, chữ display condensed in hoa (Antonio).
- **Độ hiếm**: mỗi tier có màu, tên và số pip (1 đến 4 hình thoi), nên vẫn đọc được độ hiếm khi không nhìn màu.

| Tier | Màu | Badge | Giải |
| --- | --- | --- | --- |
| Common | Bạc `oklch(84% 0.025 250)` | viền, 1 pip | Discount: Mysbox, SK, SC, VL |
| Medium rare | Mint `oklch(80% 0.15 158)` | viền, 2 pip | Discount: BK, SM, Tepo |
| Rare | Vàng `oklch(82% 0.15 78)` | nền đặc, 3 pip | Amazon gift card $50 |
| Legendary | Đỏ cam `oklch(66% 0.21 32)` | nền đặc, viền đôi, 4 pip | 3 app Qikify bất kỳ |

## Deliverables

| # | Hạng mục | File |
| --- | --- | --- |
| 1 | Hero landing desktop 1920×800 | `exports/kv-hero-desktop-1920x800.png` |
| 1 | Hero landing mobile 750×1000 | `exports/kv-hero-mobile-750x1000.png` |
| 1 | Landing page dựng sẵn (kiêm wireframe cho dev) | `index.html` + wireframe ở cuối `kit.html` |
| 2 | Nền và chi tiết custom cho trang reveal, 4 tier | `reveal.html`, `exports/reveal-<tier>-1920x1080.png`, `exports/reveal-<tier>-750x1334.png` |
| 3 | Banner in-app notification 1200×300 | `exports/inapp-banner-1200x300.png` |
| 3 | Ảnh header email/newsletter 1200×600 | `exports/email-header-1200x600.png` |
| 3 | Announcement bar 1920×56 | `exports/announcement-bar-1920x56.png` |
| 3 | Popup website 800×960 | `exports/popup-800x960.png` |
| | Board tổng: KV, các khung, badge, bảng màu, wireframe | `kit.html` |

Muốn thêm kích thước mới: thêm một khung `.f` trong `kit.html` (mọi thứ bên trong dùng `em`, chỉ cần đặt width/height), rồi mở `kit.html?frame=<tên>` để chụp ở tỉ lệ 1:1.

## Trang reveal: những gì giữ nguyên, những gì custom

- **Giữ nguyên**: hộp quà và animation unbox của Mysbox. Dev gắn nguyên khối Mysbox vào `data-slot="mysbox"` (khung nét đứt).
- **Custom**: nền tỏa màu theo tier trúng; lưới mờ 100 hộp phía sau, hộp vừa mở được viền theo màu tier; dải băng BFCM ở chân trang; badge tier dưới tên giải; nút "Claim it".
- Xem từng tier: `reveal.html?tier=common|medium|rare|legendary&box=63` (thêm `&embed` để ẩn thanh chọn tier).

## Ghi chú cho dev

- Trạng thái thật của tường hộp lấy từ API: `window.QIKIFY_BOXES = { 7: "common", 42: "rare" }` trước script. Mặc định cả 100 hộp đóng và một hộp ngẫu nhiên rung nhẹ (tắt khi người dùng bật reduced motion).
- Ảnh export dùng **trạng thái minh họa** (vài hộp đã mở) cho KV; đó không phải số liệu thật.
- Token màu và font ở `tokens.css`, component ở `campaign.css`.

## Cần bổ sung trước khi chốt

1. **Màu brand và logo Qikify**: môi trường build không truy cập được qikify.com, nên chưa khóa màu brand. Đặt mã hex thật vào `--color-brand` trong `tokens.css` và logo vào `data-slot="logo"`.
2. **Tên đầy đủ các app** (SK, SC, VL, BK, SM): hiện đang để tên viết tắt như trong brief.
3. **Mức discount** từng app, **thời gian chạy**, **số hộp mỗi store/email**, **cách gửi Amazon card**: đang để "To confirm" trong phần fine print.
4. **Screen recording Mysbox** để ghép vào khung reveal khi làm mockup cuối.
