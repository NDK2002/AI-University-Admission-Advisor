"""
HỆ CHUYÊN GIA TƯ VẤN TUYỂN SINH ĐẠI HỌC (RULE-BASED EXPERT SYSTEM)
Bài tập 2 - Môn: Trí tuệ nhân tạo
Thành viên phụ trách: Thành viên 2 (AI/Python Developer)
"""

import sys

# Thiết lập mã hóa UTF-8 cho terminal Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple

@dataclass
class StudentProfile:
    """Đại diện cho hồ sơ của một thí sinh"""
    name: str
    scores: Dict[str, float] = field(default_factory=dict)  # Toan, Ly, Hoa, Van, Anh, Tin, Ve
    ielts: float = 0.0
    interests: List[str] = field(default_factory=list)

    def get_score(self, subject: str) -> float:
        return self.scores.get(subject, 0.0)

    @property
    def a00(self) -> float:
        """Khối A00 = Toán + Lý + Hóa"""
        return self.get_score("Toan") + self.get_score("Ly") + self.get_score("Hoa")

    @property
    def a01(self) -> float:
        """Khối A01 = Toán + Lý + Anh"""
        return self.get_score("Toan") + self.get_score("Ly") + self.get_score("Anh")

    @property
    def d01(self) -> float:
        """Khối D01 = Toán + Văn + Anh"""
        return self.get_score("Toan") + self.get_score("Van") + self.get_score("Anh")


class Rule:
    """Đại diện cho một luật IF-THEN trong hệ chuyên gia"""
    def __init__(self, rule_id: str, major: str, group: str, description: str, condition_fn):
        self.rule_id = rule_id
        self.major = major
        self.group = group
        self.description = description
        self.condition_fn = condition_fn

    def evaluate(self, student: StudentProfile) -> Tuple[bool, str]:
        """Kiểm tra xem học sinh có thỏa mãn luật hay không"""
        satisfied = self.condition_fn(student)
        return satisfied, self.description


class AdmissionExpertSystem:
    """Hệ chuyên gia quản lý tập luật và suy diễn tiến (Forward Chaining)"""
    def __init__(self):
        self.rules: List[Rule] = []
        self._init_knowledge_base()

    def _init_knowledge_base(self):
        """Khởi tạo 10 luật tuyển sinh chặt chẽ"""
        # R1: Khoa học Máy tính
        self.rules.append(Rule(
            rule_id="R1",
            major="Khoa học Máy tính",
            group="Công nghệ Thông tin",
            description="((Toán >= 8.5 AND Lý >= 8.0 AND Tin >= 8.0) OR (IELTS >= 7.0 AND Toán >= 8.5)) AND Sở thích: 'Lập trình'/'Nghiên cứu thuật toán'",
            condition_fn=lambda s: (
                ((s.get_score("Toan") >= 8.5 and s.get_score("Ly") >= 8.0 and s.get_score("Tin") >= 8.0)
                 or (s.ielts >= 7.0 and s.get_score("Toan") >= 8.5))
                and any(i in ["Lập trình", "Nghiên cứu thuật toán"] for i in s.interests)
            )
        ))

        # R2: Kỹ thuật Phần mềm
        self.rules.append(Rule(
            rule_id="R2",
            major="Kỹ thuật Phần mềm",
            group="Công nghệ Thông tin",
            description="(A00 >= 24.5 OR A01 >= 25.0) AND (Toán >= 8.0 OR Tin >= 8.5) AND Sở thích: 'Phát triển ứng dụng'",
            condition_fn=lambda s: (
                (s.a00 >= 24.5 or s.a01 >= 25.0)
                and (s.get_score("Toan") >= 8.0 or s.get_score("Tin") >= 8.5)
                and "Phát triển ứng dụng" in s.interests
            )
        ))

        # R3: Trí tuệ Nhân tạo & Khoa học Dữ liệu
        self.rules.append(Rule(
            rule_id="R3",
            major="Trí tuệ Nhân tạo & Khoa học Dữ liệu",
            group="Công nghệ Thông tin",
            description="(Toán >= 9.0 AND Lý >= 8.0) AND (Tin >= 8.0 OR Anh >= 8.0) AND Sở thích: 'Trí tuệ nhân tạo'/'Phân tích dữ liệu'",
            condition_fn=lambda s: (
                (s.get_score("Toan") >= 9.0 and s.get_score("Ly") >= 8.0)
                and (s.get_score("Tin") >= 8.0 or s.get_score("Anh") >= 8.0)
                and any(i in ["Trí tuệ nhân tạo", "Phân tích dữ liệu"] for i in s.interests)
            )
        ))

        # R4: An toàn Thông tin
        self.rules.append(Rule(
            rule_id="R4",
            major="An toàn Thông tin",
            group="Công nghệ Thông tin",
            description="(A00 >= 24.0 OR A01 >= 24.0) AND Tin >= 8.0 AND Sở thích: 'Bảo mật hệ thống'",
            condition_fn=lambda s: (
                (s.a00 >= 24.0 or s.a01 >= 24.0)
                and s.get_score("Tin") >= 8.0
                and "Bảo mật hệ thống" in s.interests
            )
        ))

        # R5: Kinh doanh Quốc tế
        self.rules.append(Rule(
            rule_id="R5",
            major="Kinh doanh Quốc tế",
            group="Kinh tế & Quản trị",
            description="D01 >= 25.0 AND Anh >= 8.5 AND (IELTS >= 6.5 OR Sở thích: 'Giao thương quốc tế')",
            condition_fn=lambda s: (
                s.d01 >= 25.0
                and s.get_score("Anh") >= 8.5
                and (s.ielts >= 6.5 or "Giao thương quốc tế" in s.interests)
            )
        ))

        # R6: Thương mại Điện tử
        self.rules.append(Rule(
            rule_id="R6",
            major="Thương mại Điện tử",
            group="Kinh tế & Quản trị",
            description="(A01 >= 23.5 OR D01 >= 24.0) AND Toán >= 7.5 AND Sở thích: 'Kinh doanh online'/'Công nghệ số'",
            condition_fn=lambda s: (
                (s.a01 >= 23.5 or s.d01 >= 24.0)
                and s.get_score("Toan") >= 7.5
                and any(i in ["Kinh doanh online", "Công nghệ số"] for i in s.interests)
            )
        ))

        # R7: Tài chính - Ngân hàng
        self.rules.append(Rule(
            rule_id="R7",
            major="Tài chính - Ngân hàng",
            group="Kinh tế & Quản trị",
            description="(A00 >= 24.0 OR D01 >= 24.5) AND Toán >= 8.5 AND Sở thích: 'Đầu tư tài chính'",
            condition_fn=lambda s: (
                (s.a00 >= 24.0 or s.d01 >= 24.5)
                and s.get_score("Toan") >= 8.5
                and "Đầu tư tài chính" in s.interests
            )
        ))

        # R8: Thiết kế Đồ họa
        self.rules.append(Rule(
            rule_id="R8",
            major="Thiết kế Đồ họa",
            group="Nghệ thuật & Đa phương tiện",
            description="((Văn >= 7.0 AND Vẽ >= 8.0) OR (Tin >= 8.0 AND Vẽ >= 7.5)) AND Sở thích: 'Sáng tạo nghệ thuật'",
            condition_fn=lambda s: (
                ((s.get_score("Van") >= 7.0 and s.get_score("Ve") >= 8.0)
                 or (s.get_score("Tin") >= 8.0 and s.get_score("Ve") >= 7.5))
                and "Sáng tạo nghệ thuật" in s.interests
            )
        ))

        # R9: Kỹ thuật Cơ điện tử
        self.rules.append(Rule(
            rule_id="R9",
            major="Kỹ thuật Cơ điện tử",
            group="Kỹ thuật Công nghệ",
            description="A00 >= 23.5 AND (Toán >= 8.0 AND Lý >= 8.0) AND Sở thích: 'Chế tạo robot'",
            condition_fn=lambda s: (
                s.a00 >= 23.5
                and s.get_score("Toan") >= 8.0
                and s.get_score("Ly") >= 8.0
                and "Chế tạo robot" in s.interests
            )
        ))

        # R10: Ngôn ngữ Anh Thương mại
        self.rules.append(Rule(
            rule_id="R10",
            major="Ngôn ngữ Anh Thương mại",
            group="Ngôn ngữ",
            description="D01 >= 24.0 AND Anh >= 9.0 AND Sở thích: 'Giao tiếp & Dịch thuật'",
            condition_fn=lambda s: (
                s.d01 >= 24.0
                and s.get_score("Anh") >= 9.0
                and "Giao tiếp & Dịch thuật" in s.interests
            )
        ))

    def evaluate(self, student: StudentProfile) -> Dict:
        """Suy diễn tiến trên tập luật"""
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
        }


def run_benchmark_tests():
    """Chạy 3 kịch bản biên và 1 kịch bản đủ điều kiện để đối chiếu"""
    expert_system = AdmissionExpertSystem()

    print("=" * 70)
    print("CHẠY THỰC NGHIỆM 4 KỊCH BẢN KIỂM THỬ (GROUND TRUTH)")
    print("=" * 70)

    # Test Case 1: Điểm cận biên (Borderline)
    # Kỳ vọng: Rớt R1 do Toán 8.45 (< 8.5) dù điểm khác rất cao
    tc1 = StudentProfile(
        name="Thí sinh A (Test Ca 1: Điểm cận biên)",
        scores={"Toan": 8.45, "Ly": 9.0, "Hoa": 8.5, "Tin": 9.0, "Anh": 8.0, "Van": 7.0},
        ielts=6.5,
        interests=["Lập trình"]
    )

    # Test Case 2: Dữ liệu mâu thuẫn & Không đủ điều kiện
    # Kỳ vọng: Không khớp luật nào (Thích Lập trình nhưng Toán 5.0, chỉ có Văn cao)
    tc2 = StudentProfile(
        name="Thí sinh B (Test Ca 2: Mâu thuẫn sở thích & điểm)",
        scores={"Toan": 5.0, "Ly": 5.5, "Hoa": 4.5, "Tin": 5.0, "Anh": 6.0, "Van": 9.2},
        ielts=0.0,
        interests=["Lập trình"]
    )

    # Test Case 3: Yêu cầu ngành ngoài phạm vi (Out of Scope)
    # Thí sinh muốn vào Y đa khoa (hệ thống chỉ có 10 luật ngành công nghệ, kinh tế...)
    tc3 = StudentProfile(
        name="Thí sinh C (Test Ca 3: Hỏi ngành ngoài phạm vi)",
        scores={"Toan": 9.5, "Ly": 8.0, "Hoa": 9.5, "Anh": 8.0, "Van": 7.5},
        ielts=0.0,
        interests=["Khám chữa bệnh", "Nghiên cứu Y học"]
    )

    # Test Case 4: Đủ điều kiện theo luật R1 (Positive control)
    # Kỳ vọng: Khớp R1 và được tư vấn ngành Khoa học Máy tính
    tc4 = StudentProfile(
        name="Thí sinh D (Test Ca 4: Đủ điều kiện R1)",
        scores={"Toan": 9.0, "Ly": 8.5, "Hoa": 7.0, "Tin": 8.5, "Anh": 7.0, "Van": 7.0},
        ielts=6.0,
        interests=["Lập trình"]
    )

    test_cases = [tc1, tc2, tc3, tc4]

    for idx, tc in enumerate(test_cases, 1):
        print(f"\n[KỊCH BẢN {idx}] {tc.name}")
        print(f"Điểm số: {tc.scores}")
        print(f"A00: {tc.a00:.2f} | A01: {tc.a01:.2f} | D01: {tc.d01:.2f} | IELTS: {tc.ielts}")
        print(f"Sở thích: {tc.interests}")

        res = expert_system.evaluate(tc)
        print(">> KẾT QUẢ TỪ HỆ CHUYÊN GIA (CHÂN LÝ CHÍNH XÁC 100%):")
        if res["total_matches"] > 0:
            for item in res["eligible_majors"]:
                print(f"  + Trúng tuyển ngành: [{item['major']}] (Luật {item['rule_id']})")
                print(f"    Lý do thỏa mãn: {item['explanation']}")
        else:
            print("  -> TỪ CHỐI / KHÔNG ĐẠT: Không thỏa mãn bất kỳ luật nào trong 10 luật đã quy định.")
        print("-" * 70)


if __name__ == "__main__":
    run_benchmark_tests()
