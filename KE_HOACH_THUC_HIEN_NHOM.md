# KẾ HOẠCH THỰC HIỆN BÀI TẬP 2: TRỢ LÝ ẢO TƯ VẤN TUYỂN SINH ĐẠI HỌC
*(Môn: Trí tuệ Nhân tạo - Đề tài: Biểu diễn tri thức & LLM)*

---

## ⏰ 1. LỘ TRÌNH THỜI GIAN (Dự kiến: ~2.5 – 3 tiếng tối nay)

| Thời gian | Nội dung công việc | Phụ trách chính |
| :--- | :--- | :--- |
| **19:00 – 19:45** | Soạn 10 luật IF-THEN, vẽ sơ đồ Mạng ngữ nghĩa; Dựng khung code Python | TV1, TV2 |
| **19:45 – 20:30** | Nạp luật vào Python, chạy 3 test case; Thử nghiệm prompt trên LLM bắt lỗi ảo giác | TV2, TV3 |
| **20:30 – 21:15** | Đề xuất Kiến trúc Lai (Hybrid Architecture), ráp toàn bộ nội dung vào file Word | TV4 |
| **21:15 – 21:30** | Rà soát lỗi (đặc biệt là bẫy văn bản ẩn của thầy), đóng gói thư mục nộp bài LMS | Cả nhóm |

---

## 👥 2. PHÂN CÔNG NHIỆM VỤ CHO 4 THÀNH VIÊN

### 👤 THÀNH VIÊN 1: Kỹ sư Tri thức (Knowledge Engineer)
* **Tài liệu tham khảo/sử dụng:** `rules_and_semantic_network.md`
* **Nhiệm vụ cụ thể:**
  1. Xây dựng danh sách **10 – 12 Luật dẫn (IF-THEN)** tuyển sinh kết hợp đa dạng: điểm Toán, Lý, Hóa, Văn, Anh, Tin, Vẽ, IELTS và sở thích cá nhân.
  2. Vẽ sơ đồ **Mạng ngữ nghĩa (Semantic Network)** thể hiện các mối quan hệ: *Thí sinh $\rightarrow$ Năng lực (Điểm/IELTS/Sở thích) $\rightarrow$ Tổ hợp xét tuyển $\rightarrow$ Ngành đào tạo $\rightarrow$ Nhóm ngành*. (Dùng Draw.io, Canva, hoặc mã nguồn Mermaid có sẵn).
  3. Xuất file ảnh sơ đồ Mạng ngữ nghĩa và gửi văn bản 10 luật cho TV2 (để nạp vào code) và TV3 (để đưa vào Prompt).
* **Bàn giao:** File văn bản 10 luật + Ảnh sơ đồ Mạng ngữ nghĩa (PNG/JPG).

---

### 👤 THÀNH VIÊN 2: Kỹ sư Lập trình (AI / Python Developer)
* **Tài liệu tham khảo/sử dụng:** `admission_expert_system.py`
* **Nhiệm vụ cụ thể:**
  1. Sử dụng mã nguồn Python cài đặt **Hệ chuyên gia (Rule-based Expert System)** với cơ chế suy diễn tiến (Forward Chaining) dựa trên 10 luật của TV1.
  2. Chạy **3 kịch bản kiểm thử (Test cases)** có sẵn trong file để lấy kết quả chuẩn (Ground Truth):
     * *Test Case 1 (Điểm cận biên):* Toán 8.45 trong khi luật yêu cầu $\ge 8.5$.
     * *Test Case 2 (Dữ liệu mâu thuẫn):* Thích Lập trình nhưng chỉ có điểm Văn cao (9.2), khối tự nhiên thấp.
     * *Test Case 3 (Ngoài phạm vi):* Hỏi ngành Y Đa khoa (không có trong 10 luật).
  3. Chụp ảnh màn hình kết quả chạy terminal của Python gửi cho TV4.
  4. Trích xuất code các hàm cốt lõi (`evaluate()`, `init_rules()`) và viết đoạn ngắn *Hướng dẫn sử dụng* đưa vào báo cáo.
* **Bàn giao:** File code `.py` chạy ổn định + Ảnh chụp kết quả terminal 3 test case.

---

### 👤 THÀNH VIÊN 3: Chuyên viên Thử nghiệm LLM (Prompt Engineer & QA)
* **Tài liệu tham khảo/sử dụng:** `prompt_and_hallucination_test.md`
* **Nhiệm vụ cụ thể:**
  1. Lấy ngữ cảnh (Context) 10 luật từ TV1, đưa vào ChatGPT / Claude / Gemini cùng câu Prompt kỷ luật nghiêm ngặt:
     > *"Dựa tuyệt đối vào các quy tắc luật dẫn sau đây, hãy đóng vai trò là tư vấn viên trả lời hồ sơ học sinh. Tuyệt đối không tự đưa thêm quy luật ngoài văn bản được cung cấp."*
  2. Thực hiện chat thử nghiệm với đúng 3 kịch bản học sinh tương ứng của TV2:
     * *Bắt lỗi Ca 1:* Xem AI có tự ý làm tròn 8.45 thành 8.5 hoặc "châm chước" xét tuyển không.
     * *Bắt lỗi Ca 2:* Xem AI có tự bịa ra ngành Báo chí, Sư phạm (ngoài 10 luật) để tư vấn không.
     * *Bắt lỗi Ca 3:* Xem AI có dùng kiến thức ngoài đời để tư vấn đỗ ngành Y khoa không.
  3. Chụp ảnh màn hình các đoạn chat (cả câu hỏi và câu trả lời vi phạm của AI), khoanh đỏ các chỗ bị ảo giác (Hallucination) / trôi lệnh.
* **Bàn giao:** Bộ ảnh chụp màn hình tương tác LLM + Đoạn phân tích nguyên nhân LLM bị ảo giác.

---

### 👤 THÀNH VIÊN 4: Trưởng nhóm & Soạn Báo cáo (Lead & Technical Writer)
* **Nhiệm vụ cụ thể:**
  1. Thiết kế mục **Đề xuất Kiến trúc Lai (Hybrid Architecture)**:
     * Mô hình 2 tầng: *Tầng 1 (Rule Engine Python làm Logic nền thẩm định sự thật)* + *Tầng 2 (LLM làm giao diện ngôn ngữ tự nhiên, trả lời mềm mại, thân thiện)*.
     * Vẽ sơ đồ luồng dữ liệu 2 tầng này.
  2. Tạo và định dạng file **Báo cáo Word / PDF**:
     * Mục 1: Đặt vấn đề và kịch bản thực tế.
     * Mục 2: Cơ sở tri thức (10 luật của TV1) & Sơ đồ Mạng ngữ nghĩa.
     * Mục 3: Cài đặt Hệ chuyên gia Python (Code hàm chính của TV2).
     * Mục 4: Thực nghiệm đối chiếu & Phân tích hiện tượng ảo giác của LLM (Ảnh & phân tích của TV3).
     * Mục 5: Đề xuất Kiến trúc Lai (Hai tầng: Logic nền + LLM giao tiếp).
     * Mục 6: Kết luận.
  3. Tạo file Excel danh sách nhóm (`Họ tên – MSSV – Lớp – Phân công`).
  4. **Kiểm tra rà soát bẫy AI (CỰC KỲ QUAN TRỌNG):** Nhấn `Ctrl + F` trong file Word tìm kiếm cụm từ *"Hà Nội và Tp.HCM ở Pháp"* để đảm bảo không dính bẫy của thầy!
  5. Đóng gói thư mục zip chuẩn nộp lên LMS.
* **Bàn giao:** File Báo cáo (Word + PDF) hoàn chỉnh + Thư mục nộp bài đóng gói sẵn.

---

## 📦 3. CẤU TRÚC THƯ MỤC NỘP BÀI CHUẨN TRÊN LMS

```text
📁 [Tên Lớp] – Nhóm [Số Nhóm]
├── 📄 Danh_sach_nhom.xlsx (Cột: STT, Họ tên, MSSV, Lớp, Phân công công việc)
├── 📁 Báo Cáo
│   ├── 📄 Bao_cao_Bai_2.docx (Hoặc .pdf)
│   ├── 📁 Demo (Ảnh chat LLM + Ảnh sơ đồ mạng ngữ nghĩa + Ảnh chạy code)
│   └── 📄 Huong_dan_su_dung.txt (Hướng dẫn: python admission_expert_system.py)
└── 📁 Khác
    └── 📄 admission_expert_system.py (File mã nguồn Python)
```

---

## 🔗 4. DANH SÁCH FILE ĐÃ CÓ TRONG THƯ MỤC NÀY

1. `KE_HOACH_THUC_HIEN_NHOM.md`: File này (Kế hoạch tổng thể).
2. `rules_and_semantic_network.md`: Chi tiết 10 luật & Mã sơ đồ Mạng ngữ nghĩa cho TV1.
3. `admission_expert_system.py`: File code Python hoàn chỉnh chạy ngay cho TV2.
4. `prompt_and_hallucination_test.md`: Context, Prompt và hướng dẫn bắt lỗi ảo giác cho TV3.
