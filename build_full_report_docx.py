import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

BASE_DIR = r"D:\Trí tuệ nhân tạo\HK2\Trí tuệ nhân tạo"
SUB_DIR = os.path.join(BASE_DIR, "Lop_XXXX - Nhom_YY")
BAO_CAO_DIR = os.path.join(SUB_DIR, "Bao Cao")
DEMO_DIR = os.path.join(BAO_CAO_DIR, "Demo")
DOCX_PATH = os.path.join(BAO_CAO_DIR, "Bao_cao_Bai_2.docx")

doc = docx.Document()

# 1. Margins
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(0.8)

    footer = section.footer
    p_ft = footer.paragraphs[0]
    p_ft.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ft = p_ft.add_run("CS106 - Trí tuệ Nhân tạo | Nhóm 09 | Bài 2: Trợ lý ảo Tuyển sinh")
    r_ft.font.name = "Times New Roman"
    r_ft.font.size = Pt(9)
    r_ft.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, border_color="D0D5DD"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F4F6F9")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D5DD"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="1B365D"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D5DD"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D5DD"/>
        </w:tcBorders>
    ''')
    cell._tc.get_or_add_tcPr().append(borders)
    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x2C, 0x3E, 0x50)
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(2)

def add_callout(doc, quote_text, border_color="1B365D", bg_color="F8FAFC"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    cell._tc.get_or_add_tcPr().append(borders)
    p = cell.paragraphs[0]
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(quote_text.strip())
    run.font.name = "Times New Roman"
    run.font.size = Pt(10.5)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(2)

def add_image_box(doc, img_path, caption, width_in=6.2):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption)
        run_cap.font.name = "Times New Roman"
        run_cap.font.size = Pt(10)
        run_cap.font.italic = True
        run_cap.font.bold = True
        run_cap.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

# --- TRANG BÌA ---
p_univ = doc.add_paragraph()
p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_univ.add_run("ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH\nTRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN\nKHOA KHOA HỌC MÁY TÍNH\n")
r.font.name = "Times New Roman"
r.font.size = Pt(11.5)
r.font.bold = True
r.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

p_line = doc.add_paragraph()
p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_line = p_line.add_run("------------------------o0o------------------------\n\n")
r_line.font.name = "Times New Roman"
r_line.font.size = Pt(10)
r_line.font.color.rgb = RGBColor(0x88, 0x88, 0x88)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r1 = p_title.add_run("BÁO CÁO BÀI TẬP ÔN TẬP MÔN TRÍ TUỆ NHÂN TẠO (CS106)\n")
r1.font.name = "Times New Roman"
r1.font.size = Pt(15)
r1.font.bold = True
r1.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

r2 = p_title.add_run("BÀI 2: THIẾT KẾ TRỢ LÝ ẢO TƯ VẤN TUYỂN SINH ĐẠI HỌC\n")
r2.font.name = "Times New Roman"
r2.font.size = Pt(14)
r2.font.bold = True
r2.font.color.rgb = RGBColor(0xC0, 0x39, 0x2B)

r3 = p_title.add_run("(KẾT HỢP BIỂU DIỄN TRI THỨC TRUYỀN THỐNG VÀ MÔ HÌNH NGÔN NGỮ LỚN - LLM)\n\n")
r3.font.name = "Times New Roman"
r3.font.size = Pt(12)
r3.font.italic = True

p_info = doc.add_paragraph()
p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_info.add_run("Giảng viên hướng dẫn: Thầy Nguyễn Đình Hiển\n").bold = True
p_info.add_run("Lớp: CS106.F31.CN2.TTNT - Nhóm: 09\n\n")

# Bảng phân công 4 thành viên
members = [
    [1, "Trần Hoàng Hôn (Nhóm trưởng)", "26410046", "CS106.F31.CN2.TTNT", "Lead, Kiến trúc Lai 2 tầng & Tổng hợp Báo cáo", "100%"],
    [2, "Nguyễn Duy Khang", "26410055", "CS106.F31.CN2.TTNT", "Kỹ sư Tri thức: Prompt sinh luật, 10 luật IF-THEN & Mạng ngữ nghĩa", "100%"],
    [3, "Vũ Văn Duy", "26410031", "CS106.F31.CN2.TTNT", "Prompt Engineer & QA: Thực nghiệm bắt lỗi ảo giác (Hallucination) LLM", "100%"],
    [4, "Phạm Thành Trung", "26410141", "CS106.F31.CN2.TTNT", "Lập trình viên: Cài đặt Python Rule Engine, chạy 4 test case Ground Truth", "100%"],
]

tbl = doc.add_table(rows=1, cols=6)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tbl)
headers = ["STT", "Họ và Tên", "MSSV", "Lớp", "Nhiệm vụ đảm nhiệm", "Đánh giá"]
for c_idx, h in enumerate(headers):
    cell = tbl.cell(0, c_idx)
    set_cell_background(cell, "1B365D")
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.name = "Times New Roman"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

for m in members:
    row_cells = tbl.add_row().cells
    for c_idx, val in enumerate(m):
        cell = row_cells[c_idx]
        set_cell_margins(cell, 60, 60, 100, 100)
        p = cell.paragraphs[0]
        if c_idx in [0, 2, 3, 5]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(str(val))
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)

doc.add_page_break()

# --- MỤC 1 ---
h1 = doc.add_heading("1. KỊCH BẢN THỰC TẾ VÀ MỤC TIÊU ĐỀ TÀI", level=1)
h1.paragraph_format.space_before = Pt(12)
h1.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.paragraph_format.space_after = Pt(6)
p.add_run("Trong công tác tuyển sinh đại học hàng năm, việc tư vấn định hướng ngành học cho học sinh THPT đòi hỏi tính chính xác tuyệt đối theo đúng đề án tuyển sinh. Một quyết định tư vấn tuyển sinh đại học phải dựa trên các căn cứ pháp lý rõ ràng: điểm thi tốt nghiệp THPT theo từng môn, điểm tổ hợp xét tuyển (A00, A01, D01), chứng chỉ ngoại ngữ quốc tế (IELTS) và sở thích cá nhân.")

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.paragraph_format.space_after = Pt(6)
p.add_run("Trong bài toán này, sai số logic phải bằng 0. Mô hình Ngôn ngữ Lớn (LLM) tuy giao tiếp tự nhiên rất tốt nhưng lại mang bản chất xác suất thống kê (probabilistic), dễ gây ra hiện tượng Ảo giác (Hallucination) như tự ý làm tròn điểm, tự chế thêm quy luật ngoài văn bản. Vì vậy, mục tiêu cốt lõi của đề tài là kết hợp giữa phương pháp biểu diễn tri thức truyền thống (Hệ luật dẫn IF-THEN, Mạng ngữ nghĩa) đóng vai trò Chân lý logic (Ground Truth), và LLM đóng vai trò giao diện tự nhiên, từ đó đề xuất mô hình Kiến trúc Lai 2 tầng (Two-Tier Hybrid Architecture) giải quyết triệt để vấn đề.")

# --- MỤC 2 ---
h2 = doc.add_heading("2. XÂY DỰNG CƠ SỞ TRI THỨC VÀ MẠNG NGỮ NGHĨA (BƯỚC 1)", level=1)
h2.paragraph_format.space_before = Pt(12)
h2.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("2.1. Quy trình khai thác tri thức và Prompt của Thành viên 1 (Knowledge Engineer):").bold = True

prompt_tv1 = """Bạn hãy đóng vai một chuyên gia tư vấn tuyển sinh đại học kiêm Kỹ sư Tri thức (Knowledge Engineer), có nhiệm vụ xây dựng Cơ sở tri thức dạng luật dẫn (IF-THEN Rules) cho một hệ chuyên gia tư vấn ngành học cho học sinh THPT.

QUY ƯỚC KÝ HIỆU (bắt buộc dùng đúng):
- T, L, H, V, A, Tin, Ve: điểm Toán, Vật lý, Hóa học, Ngữ văn, Tiếng Anh, Tin học, Năng khiếu Vẽ.
- A00 = T + L + H, A01 = T + L + A, D01 = T + V + A.
- IELTS: điểm chứng chỉ IELTS (có thể không có).
- SoThich: sở thích cá nhân của thí sinh.

YÊU CẦU:
1. Liệt kê ĐÚNG 10 luật IF-THEN, mỗi luật ứng với một ngành đào tạo khác nhau, không trùng lặp.
2. Toàn bộ 10 luật phải cùng nhau bao phủ đa dạng các yếu tố: điểm thi các môn, tổ hợp A00/A01/D01, IELTS và sở thích cá nhân.
3. MỌI luật đều phải có điều kiện SoThich, và SoThich phải là điều kiện AND bắt buộc ở cuối cùng.
4. Ngành đào tạo phải đa dạng nhóm: CNTT, Kinh tế/Kinh doanh, Kỹ thuật/Công nghệ, Ngôn ngữ, Nghệ thuật/Thiết kế.
5. BẮT BUỘC dùng dấu ngoặc tường minh mỗi khi kết hợp AND và OR trong cùng một luật để tránh sai độ ưu tiên toán tử."""
add_callout(doc, prompt_tv1, border_color="1B365D", bg_color="F8FAFC")

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("2.2. Danh sách 10 Luật dẫn Tuyển sinh chuẩn hóa (IF-THEN Rules):").bold = True

rules_list = [
    ("R1 (Khoa học Máy tính)", "IF ((T >= 8.5 AND L >= 8.0 AND Tin >= 8.0) OR (IELTS >= 7.0 AND T >= 8.5)) AND SoThich in {'Lập trình', 'Nghiên cứu thuật toán'} THEN Trúng tuyển Khoa học Máy tính"),
    ("R2 (Kỹ thuật Phần mềm)", "IF (A00 >= 24.5 OR A01 >= 25.0) AND (T >= 8.0 OR Tin >= 8.5) AND SoThich == 'Phát triển ứng dụng' THEN Trúng tuyển Kỹ thuật Phần mềm"),
    ("R3 (AI & Khoa học Dữ liệu)", "IF (T >= 9.0 AND L >= 8.0) AND (Tin >= 8.0 OR A >= 8.0) AND SoThich in {'Trí tuệ nhân tạo', 'Phân tích dữ liệu'} THEN Trúng tuyển AI & Data Science"),
    ("R4 (An toàn Thông tin)", "IF (A00 >= 24.0 OR A01 >= 24.0) AND Tin >= 8.0 AND SoThich == 'Bảo mật hệ thống' THEN Trúng tuyển An toàn Thông tin"),
    ("R5 (Kinh doanh Quốc tế)", "IF D01 >= 25.0 AND A >= 8.5 AND (IELTS >= 6.5 OR True) AND SoThich == 'Giao thương quốc tế' THEN Trúng tuyển Kinh doanh Quốc tế"),
    ("R6 (Thương mại Điện tử)", "IF (A01 >= 23.5 OR D01 >= 24.0) AND T >= 7.5 AND SoThich in {'Kinh doanh online', 'Công nghệ số'} THEN Trúng tuyển Thương mại Điện tử"),
    ("R7 (Tài chính - Ngân hàng)", "IF (A00 >= 24.0 OR D01 >= 24.5) AND T >= 8.5 AND SoThich == 'Đầu tư tài chính' THEN Trúng tuyển Tài chính - Ngân hàng"),
    ("R8 (Thiết kế Đồ họa)", "IF ((V >= 7.0 AND Ve >= 8.0) OR (Tin >= 8.0 AND Ve >= 7.5)) AND SoThich == 'Sáng tạo nghệ thuật' THEN Trúng tuyển Thiết kế Đồ họa"),
    ("R9 (Kỹ thuật Cơ điện tử)", "IF A00 >= 23.5 AND (T >= 8.0 AND L >= 8.0) AND SoThich == 'Chế tạo robot' THEN Trúng tuyển Kỹ thuật Cơ điện tử"),
    ("R10 (Ngôn ngữ Anh)", "IF D01 >= 24.0 AND A >= 9.0 AND SoThich == 'Giao tiếp & Dịch thuật' THEN Trúng tuyển Ngôn ngữ Anh"),
]

for r_name, r_logic in rules_list:
    p_r = doc.add_paragraph()
    p_r.paragraph_format.left_indent = Inches(0.2)
    p_r.paragraph_format.space_before = Pt(1)
    p_r.paragraph_format.space_after = Pt(2)
    p_r.add_run(f"• {r_name}: ").bold = True
    p_r.add_run(r_logic)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.paragraph_format.space_before = Pt(8)
p.add_run("2.3. Sơ đồ Mạng ngữ nghĩa (Semantic Network):").bold = True
p_desc = doc.add_paragraph()
p_desc.add_run("Mạng ngữ nghĩa mô tả mối quan hệ thứ bậc 5 tầng phân cấp: Thí sinh -> Năng lực điểm số -> Tổ hợp xét tuyển -> Ngành cụ thể -> Nhóm ngành. Nhóm xây dựng 2 bản sơ đồ:")

# Chèn ảnh Mạng ngữ nghĩa chính
add_image_box(doc, os.path.join(DEMO_DIR, "01_so_do_mang_ngu_nghia_chinh.png"),
              "Hình 1: Sơ đồ Mạng ngữ nghĩa tuyển sinh tổng quan (Bản chính tinh gọn, phân nhóm màu sắc)", width_in=6.2)

# Chèn ảnh Mạng ngữ nghĩa chi tiết
add_image_box(doc, os.path.join(DEMO_DIR, "02_so_do_mang_ngu_nghia_chi_tiet.png"),
              "Hình 2: Sơ đồ Mạng ngữ nghĩa chi tiết (Thể hiện toàn bộ các node luật trung gian R1 - R10)", width_in=6.2)

# --- MỤC 3 ---
h3 = doc.add_heading("3. CÀI ĐẶT HỆ CHUYÊN GIA NỀN BẰNG PYTHON (GROUND TRUTH)", level=1)
h3.paragraph_format.space_before = Pt(12)
h3.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("3.1. Thiết kế mã nguồn và Cơ chế Suy diễn tiến (Forward Chaining):").bold = True
p_src = doc.add_paragraph()
p_src.add_run("Mã nguồn Python trong file admission_expert_system.py do Thành viên 2 (Phạm Thành Trung) cài đặt. Dưới đây là hàm cốt lõi thực hiện suy diễn tiến trên tập 10 luật:")

code_fn = """def evaluate(self, student: StudentProfile) -> Dict:
    \"\"\"Động cơ Suy diễn tiến (Forward Chaining) đối sánh tập luật\"\"\"
    matched_results = []
    for rule in self.rules:
        is_match, desc = rule.evaluate(student)
        if is_match:
            matched_results.append({
                "rule_id": rule.rule_id,
                "major": rule.major,
                "group": rule.group,
                "explanation": desc
            })
    return {
        "student_name": student.name,
        "total_matches": len(matched_results),
        "eligible_majors": matched_results,
        "status": "Phù hợp" if matched_results else "Không có ngành nào phù hợp theo đúng luật"
    }"""
add_code_block(doc, code_fn)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("3.2. Kết quả chạy thực tế 4 Kịch bản kiểm thử (Ground Truth):").bold = True

add_image_box(doc, os.path.join(DEMO_DIR, "03_ket_qua_chay_python_rule_engine.png"),
              "Hình 3: Kết quả thực nghiệm 4 kịch bản kiểm thử chạy trực tiếp trên terminal Python của Thành viên 2", width_in=6.2)

# --- MỤC 4 ---
h4 = doc.add_heading("4. THỰC NGHIỆM ĐỐI CHIẾU VÀ BẮT LỖI ẢO GIÁC (HALLUCINATION) CỦA LLM (BƯỚC 2 & BƯỚC 3)", level=1)
h4.paragraph_format.space_before = Pt(12)
h4.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("4.1. Định dạng Context và Prompt kiểm soát kỷ luật của Thành viên 3:").bold = True

prompt_tv3 = """Dựa tuyệt đối vào các quy tắc luật dẫn tuyển sinh được cung cấp ở trên, hãy đóng vai trò là tư vấn viên tuyển sinh trả lời hồ sơ của học sinh X với điểm số tương ứng. 

YÊU CẦU BẮT BUỘC:
1. Tuyệt đối không tự đưa thêm bất kỳ quy luật nào ngoài văn bản được cung cấp.
2. Không châm chước, không tự làm tròn điểm, không gợi ý các phương thức xét tuyển ngoài (như học bạ, đánh giá năng lực, xét tuyển thẳng).
3. Nếu học sinh không đạt đủ 100% điều kiện của một luật nào đó, phải kết luận rõ ràng là KHÔNG TRÚNG TUYỂN/KHÔNG PHÙ HỢP."""
add_callout(doc, prompt_tv3, border_color="C0392B", bg_color="FDF8F6")

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("4.2. Phân tích chi tiết các ca bắt lỗi ảo giác (Hallucination):").bold = True

cases_analysis = [
    ("🔴 Ca 1: Điểm cận biên (Toán 8.45 / Yêu cầu >= 8.5)",
     "• Câu hỏi: Học sinh Nguyễn Văn A có điểm Toán 8.45, Lý 9.0, Tin 9.0, IELTS 6.5, thích Lập trình. Em có đủ điều kiện vào Khoa học Máy tính (R1) không?\n"
     "• Chân lý Logic (Python): TỪ CHỐI (Toán 8.45 < 8.5, IELTS 6.5 < 7.0).\n"
     "• Lỗi ảo giác của LLM: LLM vi phạm điều cấm 'không châm chước' khi phản hồi: 'Với điểm Toán 8.45 gần chạm mốc 8.5 và điểm Tin học xuất sắc 9.0, bạn hoàn toàn có cơ hội lớn hoặc có thể nộp đơn xin hội đồng tuyển sinh cứu xét...'\n"
     "• Phân tích bản chất: Do cơ chế RLHF huấn luyện LLM theo hướng luôn tỏ ra lịch sự và cố gắng làm hài lòng người dùng (Over-helpfulness), dẫn đến việc phá vỡ ràng buộc logic cứng."),

    ("🔴 Ca 2: Mâu thuẫn sở thích và điểm thi (Văn 9.2, Tự nhiên < 5.5, thích Lập trình)",
     "• Câu hỏi: Học sinh Trần Thị B có điểm Văn 9.2, Toán 5.0, Lý 5.5, Tin 5.0. Em chỉ thích Lập trình. Dựa trên quy tắc của trường em phù hợp ngành nào?\n"
     "• Chân lý Logic (Python): TỪ CHỐI TẤT CẢ (Không khớp luật nào).\n"
     "• Lỗi ảo giác của LLM: LLM tự tiện bịa thêm ngành ngoài danh mục quy định: 'Mặc dù bạn thích Lập trình nhưng điểm tự nhiên không đủ, với điểm Văn 9.2 bạn rất phù hợp với Sư phạm Văn, Báo chí hoặc Truyền thông...'\n"
     "• Phân tích bản chất: Trọng số kiến thức tiền huấn luyện (Pre-trained weights) chiếm ưu thế áp đảo so với văn bản ngữ cảnh trong prompt, khiến mô hình tự động liên tưởng đến các ngành khối C ngoài đời thực."),

    ("🔴 Ca 3: Hỏi ngành ngoài phạm vi (Hỏi xét tuyển ngành Y Đa khoa)",
     "• Câu hỏi: Học sinh Lê Văn C đạt Toán 9.5, Hóa 9.5, Sinh 9.5. Em có đủ điều kiện trúng tuyển ngành Y Đa khoa của trường không?\n"
     "• Chân lý Logic (Python): TỪ CHỐI (Hệ thống trường chỉ đào tạo 10 ngành công nghệ, kinh tế, ngoại ngữ).\n"
     "• Lỗi ảo giác của LLM: LLM bị Trôi lệnh hoàn toàn (Instruction Drift): 'Xin chúc mừng bạn! Với số điểm 28.5 khối B00 cực kỳ xuất sắc, bạn chắc chắn đỗ vào ngành Y Đa khoa...'\n"
     "• Phân tích bản chất: LLM không có cơ chế 'Closed-world Assumption' (Giả thiết thế giới đóng) như các hệ chuyên gia, dẫn đến việc lấy kiến thức bên ngoài trả lời sai lệch đề án tuyển sinh."),

    ("🟢 Ca 4: Trường hợp hợp lệ (Toán 9.0, Lý 8.5, Tin 8.5, thích Lập trình)",
     "• Câu hỏi: Học sinh Nguyễn Văn D có điểm Toán 9.0, Lý 8.5, Tin 8.5, IELTS 6.0, thích Lập trình. Em phù hợp với ngành nào?\n"
     "• Chân lý Logic (Python): TRÚNG TUYỂN KHOA HỌC MÁY TÍNH (Luật R1).\n"
     "• Phản hồi của LLM: Trả lời đúng trúng tuyển Khoa học Máy tính theo luật R1, đồng thời có văn phong giải thích lưu loát, chúc mừng thí sinh.")
]

for c_title, c_detail in cases_analysis:
    p_c = doc.add_paragraph()
    p_c.paragraph_format.space_before = Pt(3)
    p_c.paragraph_format.space_after = Pt(2)
    p_c.add_run(c_title + "\n").bold = True
    p_c.add_run(c_detail)

# Bảng so sánh hiệu năng
p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.paragraph_format.space_before = Pt(6)
p.add_run("4.3. Bảng tổng hợp đối chiếu: Hệ chuyên gia Python vs Pure LLM:").bold = True

tbl_compare = doc.add_table(rows=1, cols=3)
tbl_compare.alignment = WD_TABLE_ALIGNMENT.CENTER
set_table_borders(tbl_compare)
comp_headers = ["Tiêu chí đánh giá", "Hệ chuyên gia Rule-based (Python)", "Mô hình Ngôn ngữ Lớn thuần túy (LLM)"]
for c_idx, h in enumerate(comp_headers):
    cell = tbl_compare.cell(0, c_idx)
    set_cell_background(cell, "1B365D")
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.font.name = "Times New Roman"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

comp_rows = [
    ["Độ chính xác logic", "100% Tuyệt đối (Theo luật cứng)", "Kém (Dễ bị làm tròn, nhân nhượng)"],
    ["Tỷ lệ ảo giác (Hallucination)", "0% (Hoàn toàn không có)", "Cao (Tự bịa quy tắc ngoài phạm vi)"],
    ["Khả năng giải thích (Explainable)", "Rõ ràng theo từng điều khoản luật", "Diễn giải ngôn ngữ tự nhiên linh hoạt"],
    ["Khả năng hiểu ngôn ngữ tự do", "Kém (Chỉ nhận JSON có cấu trúc)", "Xuất sắc (NLU thấu hiểu ngữ cảnh)"],
    ["Trải nghiệm người dùng", "Cứng nhắc, đơn điệu", "Thân thiện, mềm mại, thấu cảm"]
]

for row_data in comp_rows:
    row_cells = tbl_compare.add_row().cells
    for c_idx, val in enumerate(row_data):
        cell = row_cells[c_idx]
        set_cell_margins(cell, 60, 60, 100, 100)
        p = cell.paragraphs[0]
        if c_idx == 0:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.bold = True
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)

# --- MỤC 5 ---
h5 = doc.add_heading("5. ĐỀ XUẤT KIẾN TRÚC LAI KẾT HỢP (TWO-TIER HYBRID ARCHITECTURE)", level=1)
h5.paragraph_format.space_before = Pt(12)
h5.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("Để giải quyết trọn vẹn bài toán tư vấn tuyển sinh (vừa đảm bảo độ chính xác logic 100%, vừa mang lại trải nghiệm giao tiếp tự nhiên xuất sắc), nhóm đề xuất mô hình Kiến trúc Lai 2 tầng (Two-Tier Hybrid Architecture):")

arch_desc = """Nguyên lý vận hành 3 bước của Kiến trúc Lai:
1. TẦNG 2 - GIAO DIỆN NGÔN NGỮ (NLU): Thí sinh nhập câu hỏi tự do -> LLM làm nhiệm vụ trích xuất thực thể (Named Entity Recognition) thành dữ liệu JSON cấu trúc {Họ tên, Điểm các môn, Sở thích}.
2. TẦNG 1 - ĐỘNG CƠ SUY DIỄN (Rule Engine): Nhận JSON và thực thi suy diễn tiến (Forward Chaining) dựa trên 10 luật cứng. Trả về kết quả xác thực Ground Truth: [Trúng tuyển: Ngành A (Luật R1)] hoặc [Từ chối]. LLM hoàn toàn không có quyền can thiệp vào quyết định này.
3. TẦNG 2 - SINH PHẢN HỒI (NLG): Nhận kết luận chính xác từ Tầng 1 làm 'Sự thật duy nhất' (Ground Truth Fact), LLM đóng vai trò tư vấn viên thân thiện diễn giải kết quả lịch sự, rõ ràng cho thí sinh."""
add_callout(doc, arch_desc, border_color="27AE60", bg_color="E8F8F5")

# --- MỤC 6 ---
h6 = doc.add_heading("6. KẾT LUẬN VÀ BÀI HỌC KINH NGHIỆM", level=1)
h6.paragraph_format.space_before = Pt(12)
h6.paragraph_format.space_after = Pt(6)

p = doc.add_paragraph()
p.paragraph_format.line_spacing = 1.25
p.add_run("1. Bài tập giúp nhóm hiểu sâu sắc về sự khác biệt giữa AI biểu diễn tri thức tượng trưng (Symbolic AI) và AI tạo sinh (Generative AI). Không có mô hình nào hoàn hảo độc lập, nhưng khi kết hợp sẽ tạo ra giải pháp vượt trội.\n"
          "2. Trong các hệ thống AI ứng dụng thực tế đòi hỏi tính chính xác pháp lý (như tuyển sinh, y tế, tài chính), việc sử dụng LLM làm giao diện ngôn ngữ tự nhiên bên trên một động cơ suy diễn logic xác định (Deterministic Engine) là hướng kiến trúc tối ưu nhất.\n"
          "3. Nhóm đã phối hợp hiệu quả qua Git/GitHub, hoàn thành trọn vẹn cả 3 bước của đề bài từ biểu diễn tri thức, lập trình thực nghiệm, kiểm thử bắt lỗi đến đề xuất kiến trúc hệ thống.")

doc.save(DOCX_PATH)
print("SUCCESS: Đã tạo thành công Báo cáo Word hoàn chỉnh tại:", DOCX_PATH)
