# Hệ Chuyên Gia Tư Vấn Tuyển Sinh Đại Học (Rule-Based & LLM)
> **Môn học:** Trí tuệ Nhân tạo  
> **Bài tập:** Bài 2 - Biểu diễn tri thức & Mô hình Ngôn ngữ Lớn (LLM)  
> **Giảng viên hướng dẫn:** Thầy Nguyễn Đình Hiển  

---

## 🎯 Giới thiệu Dự án
Dự án xây dựng hệ thống trợ lý ảo tư vấn tuyển sinh đại học kết hợp giữa:
1. **Hệ chuyên gia truyền thống (Rule-based Expert System):** Sử dụng 10+ luật dẫn (IF-THEN) với cơ chế suy diễn tiến (Forward Chaining) và Mạng ngữ nghĩa (Semantic Network) để đảm bảo độ chính xác logic tuyệt đối (Zero Hallucination).
2. **Mô hình Ngôn ngữ Lớn (LLM):** Đóng vai trò giao tiếp tự nhiên (NLU/NLG), đồng thời thực nghiệm phân tích hiện tượng ảo giác (Hallucination) khi đối mặt dữ liệu biên/mâu thuẫn.
3. **Kiến trúc Lai 2 tầng (Two-Tier Hybrid Architecture):** Kết hợp tối ưu giữa độ chính xác của Rule Engine và sự linh hoạt, thân thiện của LLM.

---

## 👥 Phân công Nhiệm vụ (Nhóm 4 thành viên)

| Thành viên | Vai trò | Trách nhiệm chính | File tài liệu phụ trách |
| :--- | :--- | :--- | :--- |
| **Thành viên 1** | Kỹ sư Tri thức (Knowledge Engineer) | Thiết kế 10 luật IF-THEN, vẽ sơ đồ Mạng ngữ nghĩa | `rules_and_semantic_network.md` |
| **Thành viên 2** | Kỹ sư Lập trình (AI/Python Developer) | Lập trình Rule Engine bằng Python, chạy 3 test case | `admission_expert_system.py` |
| **Thành viên 3** | Thử nghiệm LLM (Prompt Engineer & QA) | Viết Prompt, chạy thực nghiệm bắt lỗi Hallucination trên LLM | `prompt_and_hallucination_test.md` |
| **Thành viên 4** | Lead & Báo cáo (Lead & Technical Writer) | Thiết kế Kiến trúc Lai 2 tầng, tổng hợp Báo cáo Word/PDF | `hybrid_architecture_and_report_outline.md` |

---

## 📁 Cấu trúc Thư mục

```text
├── .gitignore
├── README.md                                # Giới thiệu tổng quan dự án
├── KE_HOACH_THUC_HIEN_NHOM.md               # Kế hoạch chi tiết & lộ trình thời gian
├── rules_and_semantic_network.md            # Bộ 10 luật dẫn & Mạng ngữ nghĩa (TV1)
├── admission_expert_system.py               # Mã nguồn Python Hệ chuyên gia (TV2)
├── prompt_and_hallucination_test.md         # Kịch bản thực nghiệm bắt lỗi ảo giác LLM (TV3)
└── hybrid_architecture_and_report_outline.md# Kiến trúc lai & Khung báo cáo hoàn chỉnh (TV4)
```

---

## 🚀 Hướng dẫn Cài đặt & Chạy Thực nghiệm

### Yêu cầu:
* Python 3.8+ (Khuyến nghị Python 3.10+)

### Chạy kiểm thử Hệ chuyên gia:
```bash
python admission_expert_system.py
```
Hệ thống sẽ tự động chạy 4 kịch bản kiểm thử mẫu: 3 trường hợp biên theo đề bài (Điểm cận biên, Dữ liệu mâu thuẫn, Hỏi ngoài phạm vi) và 1 trường hợp đủ điều kiện R1 để xác nhận hệ thống có thể đưa ra kết quả phù hợp.
