import shutil
from pathlib import Path

# 1. Nhận danh sách các file gốc
danh_sach_file_goc = [
    r"C:\Users\Admin\Documents\GitHub\docs-uml\temp\05-sequence\UML-Sequence.png",
    r"C:\Users\Admin\Documents\GitHub\docs-uml\temp\05-sequence\UML-Sequence.puml",
    r"C:\Users\Admin\Documents\GitHub\docs-uml\temp\05-sequence\UML-Sequence.tex",
]

# 2. Danh sách các đuôi file cần thêm vào
cac_duoi_can_them = [
    # "-sample",
    # "sample",
    # "overview",
    # ".1",
    # ".2",
    # ".3",
    # "3",
    # "xxxxxxxxxxx",
    # "..."
    # "-17",
    # "-18",
    # "-19",
    # "-20",
    # "-21",
    "-22",
    "-23",
    "-24",
    "-25",
    "-26",
    "-27",
    "-28",
    "-29",
    "-30",
    # "-31",
    # "-32",
    # "-33",
    # "-34",
    # "-35",
    # "-36",
    # "-37",
    # "-38",
    # "-39",
    # "-40",
    # "-41",
    # "-42",
    # "-43",
    # "-44",
    # "-45",
    # "-46",
    # "-47",
    # "-48",
    # "-49",
    # "-50",
    # "-51",
    # "-52",
    # "-53",
    # "-54",
    # "-55",
    # "-56",
    # "-57",
    # "-58",
    # "-59",
    # "-60",
    # "-61",
    # "-62",
    # "-63",
    # "-64",
    # "-65",
    # "-66",
    # "-67",
    # "-68",
    # "-69",
    # "-70",
    # "-71",
    # "-72",
    # "-73",
    # "-74",
    # "-75",
    # "-76",
    # "-77",
    # "-78",
    # "-79",
    # "-80",
    # "-81",
    # "-82",
    # "-83",
    # "-84",
    # "-85",
    # "-86",
    # "-87",
    # "-88",
    # "-89",
    # "-90",
    # "-91",
    # "-92",
    # "-93",
    # "-94",
    # "-95",
    # "-96",
    # "-97",
    # "-98",
    # "-99",
]


def sao_chep_file_kem_duoi(danh_sach_file, danh_sach_duoi):
    """
    Tự động sao chép danh sách file và thêm đuôi vào tên file mới.
    """
    for duong_dan_str in danh_sach_file:
        duong_dan = Path(duong_dan_str)

        # Kiểm tra xem file gốc có tồn tại không trước khi copy
        if not duong_dan.exists():
            print(f"⚠️ Cảnh báo: File không tồn tại - {duong_dan}")
            continue

        for duoi in danh_sach_duoi:
            # path.stem lấy tên file (VD: UML-UseCase-)
            # path.suffix lấy định dạng (VD: .md)
            ten_file_moi = f"{duong_dan.stem}{duoi}{duong_dan.suffix}"

            # Tạo đường dẫn mới cùng thư mục với file gốc
            duong_dan_moi = duong_dan.parent / ten_file_moi

            # Thực hiện sao chép file (giữ nguyên metadata như ngày tạo, ngày sửa)
            shutil.copy2(duong_dan, duong_dan_moi)
            print(f"✅ Đã tạo file: {duong_dan_moi}")


if __name__ == "__main__":
    # 3. Chạy hàm sao chép
    print("Bắt đầu sao chép file...\n" + "-" * 40)
    sao_chep_file_kem_duoi(danh_sach_file_goc, cac_duoi_can_them)
    print("-" * 40 + "\nHoàn tất!")
