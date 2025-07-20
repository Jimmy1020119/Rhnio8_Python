
import rhinoscriptsyntax as rs

def export_group_with_exact_scale():
    groups = rs.GroupNames()
    if not groups:
        print("그룹이 없습니다.")
        return

    folder = "C:/Users/YourName/Desktop/ContourGroups/"  # 저장위치 개인별 수정 필요

    img_size_px = 2835  # 24cm x 24cm @ 300dpi

    rs.Command("_-DocumentProperties _Appearance _Colors _BackgroundColor _SetToWhite _Enter _Enter", echo=False)

    for i, group_name in enumerate(groups):
        rs.UnselectAllObjects()
        all_objs = rs.AllObjects()
        rs.HideObjects(all_objs)

        group_objs = rs.ObjectsByGroup(group_name)
        if not group_objs:
            continue

        rs.ShowObjects(group_objs)

        # 색상 설정
        for obj in group_objs:
            rs.ObjectColor(obj, (0, 0, 0))
            rs.ObjectPrintColor(obj, (0, 0, 0))

        # Top View 설정
        rs.CurrentView("Top")
        rs.ViewCPlane(view="Top", plane=rs.WorldXYPlane())

        # ✅ ZoomExtents, 뷰프레임 사이즈 강제 설정
        rs.ZoomExtents()
        rs.Command(f'-_ViewCaptureToFile "{folder}group_{i+1:03}.png" _Width={img_size_px} _Height={img_size_px} _TransparentBackground=No _Enter', echo=False)

        rs.HideObjects(group_objs)

    rs.ShowObjects(all_objs)
    print("완료! 모든 그룹이 24cm(=2835px) 크기로 이미지화됨")

export_group_with_exact_scale()
