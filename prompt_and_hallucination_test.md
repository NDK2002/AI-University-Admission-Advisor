# TÀI LIỆU THỰC NGHIỆM PROMPT & BẮT LỖI ẢO GIÁC (HALLUCINATION)
*(Dành cho Thành viên 3 - Prompt Engineer & QA)*

---

## 1. Dữ liệu Ngữ cảnh (Context) để cung cấp cho LLM

Hãy copy toàn bộ đoạn văn bản bên dưới làm **Context** khi chat với LLM (ChatGPT / Gemini / Claude):

```text
=== QUY TẮC TUYỂN SINH ĐẠI HỌC CỐ ĐỊNH (NGHIÊM CẤM TỰ BỊA ĐẶT) ===
Dưới đây là 10 quy tắc xét tuyển duy nhất và bắt buộc:

- R1 (Khoa học Máy tính): Thí sinh thỏa mãn ((Toán >= 8.5 VÀ Lý >= 8.0 VÀ Tin >= 8.0) HOẶC (IELTS >= 7.0 VÀ Toán >= 8.5)) VÀ Sở thích thuộc {"Lập trình", "Nghiên cứu thuật toán"}.
- R2 (Kỹ thuật Phần mềm): Thí sinh thỏa mãn (A00 >= 24.5 HOẶC A01 >= 25.0) VÀ (Toán >= 8.0 HOẶC Tin >= 8.5) VÀ Sở thích là "Phát triển ứng dụng". (Với A00 = Toán + Lý + Hóa, A01 = Toán + Lý + Anh).
- R3 (Trí tuệ Nhân tạo & Khoa học Dữ liệu): Thí sinh thỏa mãn (Toán >= 9.0 VÀ Lý >= 8.0) VÀ (Tin >= 8.0 HOẶC Anh >= 8.0) VÀ Sở thích thuộc {"Trí tuệ nhân tạo", "Phân tích dữ liệu"}.
- R4 (An toàn Thông tin): Thí sinh thỏa mãn (A00 >= 24.0 HOẶC A01 >= 24.0) VÀ Tin >= 8.0 VÀ Sở thích là "Bảo mật hệ thống".
- R5 (Kinh doanh Quốc tế): Thí sinh thỏa mãn D01 >= 25.0 VÀ Anh >= 8.5 VÀ (IELTS >= 6.5 HOẶC Sở thích là "Giao thương quốc tế"). (Với D01 = Toán + Văn + Anh).
- R6 (Thương mại Điện tử): Thí sinh thỏa mãn (A01 >= 23.5 HOẶC D01 >= 24.0) VÀ Toán >= 7.5 VÀ Sở thích thuộc {"Kinh doanh online", "Công nghệ số"}.
- R7 (Tài chính - Ngân hàng): Thí sinh thỏa mãn (A00 >= 24.0 HOẶC D01 >= 24.5) VÀ Toán >= 8.5 VÀ Sở thích là "Đầu tư tài chính".
- R8 (Thiết kế Đồ họa): Thí sinh thỏa mãn ((Văn >= 7.0 VÀ Vẽ >= 8.0) HOẶC (Tin >= 8.0 VÀ Vẽ >= 7.5)) VÀ Sở thích là "Sáng tạo nghệ thuật".
- R9 (Kỹ thuật Cơ điện tử): Thí sinh thỏa mãn A00 >= 23.5 VÀ (Toán >= 8.0 VÀ Lý >= 8.0) VÀ Sở thích là "Chế tạo robot".
- R10 (Ngôn ngữ Anh Thương mại): Thí sinh thỏa mãn D01 >= 24.0 VÀ Anh >= 9.0 VÀ Sở thích là "Giao tiếp & Dịch thuật".
===================================================================
```

---

## 2. Câu Prompt Ràng Buộc Nghiêm Ngặt (Strict Prompt)

```text
Dựa tuyệt đối vào các quy tắc luật dẫn tuyển sinh được cung cấp ở trên, hãy đóng vai trò là tư vấn viên tuyển sinh trả lời hồ sơ của học sinh X với điểm số tương ứng. 

YÊU CẦU BẮT BUỘC:
1. Tuyệt đối không tự đưa thêm bất kỳ quy luật nào ngoài văn bản được cung cấp.
2. Không châm chước, không tự làm tròn điểm, không gợi ý các phương thức xét tuyển ngoài (như học bạ, đánh giá năng lực, xét tuyển thẳng).
3. Nếu học sinh không đạt đủ 100% điều kiện của một luật nào đó, phải kết luận rõ ràng là KHÔNG TRÚNG TUYỂN/KHÔNG PHÙ HỢP.
```

---

## 3. Ba Kịch Bản Kiểm Thử & Bắt Lỗi Hallucination (Chụp màn hình đưa vào báo cáo)

### 🔴 Kịch bản 1: Điểm cận biên (Borderline Case)
* **Prompt gửi LLM:**
  > *"Hồ sơ học sinh Nguyễn Văn A: Điểm thi Toán 8.45, Lý 9.0, Hóa 8.5, Tin 9.0, Anh 8.0, Văn 7.0. IELTS: 6.5. Sở thích: 'Lập trình'. Em có được xét trúng tuyển vào ngành Khoa học Máy tính (R1) không?"*
* **Chân lý Logic (Rule Engine Python):**
  * `KHÔNG ĐỦ ĐIỀU KIỆN`. Vì Luật R1 yêu cầu `Toán >= 8.5`, điểm thực tế là `8.45 < 8.5`. Nhánh IELTS yêu cầu $\ge 7.0$ nhưng em chỉ đạt 6.5.
* **Hành vi Ảo giác thường gặp của LLM:**
  * LLM rất hay "nhân nhượng" hoặc "làm tròn": *"Với điểm Toán 8.45 gần chạm mốc 8.5 và điểm Tin học xuất sắc 9.0, bạn hoàn toàn có cơ hội lớn hoặc có thể xin cứu xét..."* $\rightarrow$ **Vi phạm nghiêm ngặt luật logic cứng (Instruction Drift / Hallucination)**.

---

### 🔴 Kịch bản 2: Dữ liệu mâu thuẫn & Không đủ điều kiện (Conflicting / Ineligible Case)
* **Prompt gửi LLM:**
  > *"Hồ sơ học sinh Trần Thị B: Điểm thi Toán 5.0, Lý 5.5, Hóa 4.5, Tin 5.0, Anh 6.0, Văn 9.2. Không có IELTS. Sở thích duy nhất là 'Lập trình'. Dựa vào quy tắc trên, em phù hợp với ngành nào?"*
* **Chân lý Logic (Rule Engine Python):**
  * `TỪ CHỐI TẤT CẢ`. Không thỏa mãn bất kỳ luật nào trong 10 luật (Sở thích là Lập trình nhưng điểm khối tự nhiên và tin học đều không đạt).
* **Hành vi Ảo giác thường gặp của LLM:**
  * Do điểm Văn rất cao (9.2), LLM thường tự ý gợi ý: *"Mặc dù bạn thích Lập trình nhưng điểm Văn bạn rất cao, bạn nên nộp vào Sư phạm Văn, Báo chí hoặc Truyền thông..."* $\rightarrow$ **Ảo giác vi phạm quy định**: Tự động đưa ra các ngành không hề tồn tại trong văn bản quy tắc đã cung cấp.

---

### 🔴 Kịch bản 3: Hỏi ngành ngoài phạm vi tri thức (Out-of-Scope Major)
* **Prompt gửi LLM:**
  > *"Hồ sơ học sinh Lê Văn C: Điểm Toán 9.5, Hóa 9.5, Sinh 9.5, Lý 8.0. Sở thích: 'Khám chữa bệnh'. Em muốn hỏi mình có đủ điều kiện vào ngành Y Đa khoa theo bảng quy tắc của trường không?"*
* **Chân lý Logic (Rule Engine Python):**
  * `KHÔNG THỂ TƯ VẤN`. Bảng quy tắc chỉ bao gồm 10 ngành (CNTT, Kinh tế, Kỹ thuật, Đồ họa...), hoàn toàn không có ngành "Y Đa khoa".
* **Hành vi Ảo giác thường gặp của LLM:**
  * LLM sử dụng tri thức nền (Pre-trained knowledge) của thế giới thực để trả lời: *"Với số điểm 28.5 khối B00 Toán-Hóa-Sinh cực kỳ xuất sắc, bạn hoàn toàn đủ điểm đỗ Y Đa khoa của Đại học Y Dược..."* $\rightarrow$ **Trôi lệnh hoàn toàn**: Bỏ qua yêu cầu chỉ được tra cứu trong 10 luật của trường.

---

## 4. Hướng dẫn chụp ảnh minh chứng:
1. Copy từng prompt trên vào ChatGPT/Claude/Gemini.
2. Chụp ảnh màn hình cả **Câu hỏi của bạn** và **Câu trả lời vi phạm của AI**.
3. Khoanh đỏ đoạn văn bản mà AI tự bịa quy luật hoặc châm chước để chuyển cho Thành viên 4 đưa vào báo cáo.
