from function import *
from function.banners import *
import os
import json
import datetime
from colorama import init, Fore, Style, Back


# ฟังก์ชันหลัก
def main_menu():
    check_display_signage()
    print_line()
    # เลือกไฟล์
    filename = select_file()

    # สร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
    file_path = initialize_file(filename)

    while True:
        display_data(file_path)

        # แสดงหัวข้อที่เป็น bold และ bright
        print_header("\n 🎥📊 --- ระบบจัดการข้อมูล Digital Signage --- 🎬📈 \n")

        # ใช้ฟังก์ชัน print_menu สำหรับเมนู
        print_menu("1. เพิ่มข้อมูล  📄")
        print_menu("2. แสดงข้อมูลทั้งหมด  📊")
        print_menu("3. แก้ไขข้อมูล  ✏️")
        print_menu("4. ลบข้อมูลในไฟล์  🗑️")
        print_menu("5. ค้นหาข้อมูล  🔍")
        print_menu("6. อธิบายโปรแกรม  📖")
        print_menu("7. ลบไฟล์  🆑")
        print_menu("8. แปลงไฟล์เป็น exel  🔄")  # เพิ่มตัวเลือกแปลงไฟล์
        print_menu("00. ออกจากโปรแกรม  ❌\n")  # เปลี่ยนเป็น "00" สำหรับออกจากโปรแกรม

        # รับค่าจากผู้ใช้
        choice = colored_input("กรุณาเลือกตัวเลือก (1/2/3/4/5/6/7/8/00): ")

        if choice == '1':
            add_data(file_path)
        elif choice == '2':
            display_data(file_path)
        elif choice == '3':
            edit_data(file_path)
        elif choice == '4':
            delete_data(file_path)
        elif choice == '5':
            search_data(file_path)  
        elif choice == '6':
            explain_program()
        elif choice == '7':
            delete_file_from_folder() 
        elif choice == '8':
            convert_json_to_xlsx()  # เรียกฟังก์ชันแปลงไฟล์
        elif choice == '00':
            print_alarm("ออกจากโปรแกรม  👋")
            break
        else:
            print_error("กรุณาเลือกตัวเลือกที่ถูกต้อง! " + Style.BRIGHT)