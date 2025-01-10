import os
import json
import datetime


FOLDER_NAME = 'check'


# ฟังก์ชันตรวจสอบและสร้างโฟลเดอร์และไฟล์ถ้ายังไม่มี
def initialize_file(filename):
    # ตรวจสอบและสร้างโฟลเดอร์ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว")

    # สร้างไฟล์ในโฟลเดอร์ถ้ายังไม่มี
    file_path = os.path.join(FOLDER_NAME, filename)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)  # สร้างไฟล์พร้อมข้อมูลว่าง
        print(f"สร้างไฟล์ {file_path} เรียบร้อยแล้ว")
    else:
        print(f"ไฟล์ {file_path} มีอยู่แล้ว ไม่ต้องสร้างใหม่")

    return file_path




# ฟังก์ชันให้ผู้ใช้เลือกไฟล์
def select_file():
    try:
        list_files_in_folder()

        while True:
            file_choice = input("กรุณาเลือกหมายเลขไฟล์ หรือกรอกชื่อไฟล์ใหม่: ").strip()

            # ตรวจสอบว่าเป็นหมายเลข
            if file_choice.isdigit():
                file_choice = int(file_choice)
                files = os.listdir(FOLDER_NAME)
                if 1 <= file_choice <= len(files):
                    return files[file_choice - 1]
                else:
                    print("กรุณาเลือกหมายเลขไฟล์ที่ถูกต้อง.")
            else:
                # ตรวจสอบชื่อไฟล์ไม่ให้ว่างเปล่า
                if not file_choice:
                    print("ชื่อไฟล์ไม่สามารถว่างเปล่าได้ กรุณากรอกชื่อไฟล์ใหม่.")
                    continue

                # ตรวจสอบว่าไฟล์มีนามสกุล
                if '.' not in file_choice:
                    print("ชื่อไฟล์ต้องมีนามสกุล เช่น .txt, .json เป็นต้น กรุณากรอกใหม่.")
                    continue

                filename = file_choice
                file_path = os.path.join(FOLDER_NAME, filename)

                # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
                if os.path.exists(file_path):
                    print(f"ไฟล์ {filename} มีอยู่แล้ว ไม่ต้องสร้างใหม่.")
                    return filename
                else:
                    print(f"ไฟล์ {filename} ไม่มีในโฟลเดอร์ 'check'. สร้างไฟล์ใหม่...")
                    return filename

    except FileNotFoundError:
        print(f"ไม่พบโฟลเดอร์ '{FOLDER_NAME}' กรุณาตรวจสอบโฟลเดอร์อีกครั้ง.")
    except PermissionError:
        print("ไม่สามารถเข้าถึงโฟลเดอร์หรือไฟล์ได้ กรุณาตรวจสอบสิทธิ์การเข้าถึง.")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")





# ฟังก์ชันแสดงรายชื่อไฟล์ในโฟลเดอร์ check
def list_files_in_folder():
    # ตรวจสอบและสร้างโฟลเดอร์ 'check' ถ้ายังไม่มี
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"สร้างโฟลเดอร์ {FOLDER_NAME} เรียบร้อยแล้ว")

    print("\n--- ไฟล์ที่มีอยู่ในโฟลเดอร์ 'check' ---")
    files = os.listdir(FOLDER_NAME)
    if files:
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")
    else:
        print("ยังไม่มีไฟล์ในโฟลเดอร์")





# ฟังก์ชันเพิ่มข้อมูลใหม่
def add_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # กำหนดลำดับอัตโนมัติ
    sequence = len(data) + 1

    # รับข้อมูลจากผู้ใช้ (ตรวจสอบให้ "รายการ" และ "s/n" ไม่ว่าง)
    while True:
        item = input("กรุณาใส่รายการ: ").strip()
        if not item:
            print("กรุณาใส่รายการ ไม่สามารถปล่อยว่างได้!")
        else:
            break

    while True:
        serial_number = input("กรุณาใส่ s/n: ").strip()
        if not serial_number:
            print("กรุณาใส่ s/n ไม่สามารถปล่อยว่างได้!")
        else:
            break

    symptom = input("กรุณาใส่อาการ (ถ้าไม่มีกรอกกด Enter เพื่อใช้ค่า 'จอปกติดี'): ")

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom.strip():  # ถ้าค่าที่กรอกมาเป็นค่าว่าง
        symptom = "จอปกติดี"  # กำหนดอาการเป็น "จอปกติดี"

    screen_size = input("กรุณาใส่ขนาดจอ (ถ้าไม่ระบุให้กด Enter): ").strip()

    # ถ้าไม่กรอกขนาดจอให้กำหนดเป็น 'ไม่ระบุ'
    if not screen_size:
        screen_size = "ไม่ระบุ"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # เพิ่มข้อมูลใหม่
    new_entry = {
        "ลำดับ": sequence,
        "รายการ": item,
        "s/n": serial_number,
        "อาการ": symptom,
        "ขนาดจอ": screen_size,
        "วันที่และเวลาที่ตรวจ": timestamp
    }
    data.append(new_entry)

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("บันทึกข้อมูลสำเร็จ!")





# ฟังก์ชันแก้ไขข้อมูล
def edit_data(file_path):
    # อ่านไฟล์ถ้ามีอยู่
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

    # ถ้าไม่มีข้อมูลในไฟล์
    if not data:
        print("ไม่มีข้อมูลในระบบสำหรับการแก้ไข!")
        return

    # แสดงข้อมูลที่มีอยู่
    print("\n--- ข้อมูลที่มีอยู่ ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 100)
    for entry in data:
        print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
            entry["ลำดับ"],
            entry["รายการ"],
            entry["s/n"],
            entry["อาการ"],
            entry["ขนาดจอ"],
            entry["วันที่และเวลาที่ตรวจ"]
        ))

    # เลือกข้อมูลที่ต้องการแก้ไข
    while True:
        try:
            edit_index = int(input("\nกรุณาเลือกหมายเลขลำดับที่ต้องการแก้ไข (กรอก 00 เพื่อยกเลิก): "))

            # หากกรอก 00 ให้ยกเลิกการแก้ไข
            if edit_index == 00:
                print("ยกเลิกการแก้ไขข้อมูล.")
                return

            # ตรวจสอบว่าหมายเลขลำดับที่เลือกมีอยู่
            entry = next((entry for entry in data if entry["ลำดับ"] == edit_index), None)
            if entry:
                break
            else:
                print("หมายเลขลำดับไม่ถูกต้อง กรุณากรอกใหม่!")
        except ValueError:
            print("กรุณากรอกหมายเลขลำดับที่ถูกต้อง!")

    # แสดงข้อมูลก่อนการแก้ไข
    print(f"\n--- ข้อมูลก่อนการแก้ไข ---")
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        "ลำดับ", "รายการ", "S/N", "อาการ", "ขนาดจอ", "วันที่และเวลาที่ตรวจ"
    ))
    print("-" * 100)
    print("{:<5} {:<20} {:<15} {:<30} {:<20} {:<20}".format(
        entry["ลำดับ"],
        entry["รายการ"],
        entry["s/n"],
        entry["อาการ"],
        entry["ขนาดจอ"],
        entry["วันที่และเวลาที่ตรวจ"]
    ))

    # แก้ไขข้อมูล
    item = input(f"กรุณาใส่รายการใหม่ (ปัจจุบัน: {entry['รายการ']}): ").strip()
    serial_number = input(f"กรุณาใส่ s/n ใหม่ (ปัจจุบัน: {entry['s/n']}): ").strip()
    symptom = input(f"กรุณาใส่อาการใหม่ (ปัจจุบัน: {entry['อาการ']}): ").strip()

    # ถ้าอาการไม่กรอกให้กำหนดเป็น 'จอปกติดี'
    if not symptom:
        symptom = "จอปกติดี"

    screen_size = input(f"กรุณาใส่ขนาดจอใหม่ (ปัจจุบัน: {entry['ขนาดจอ']}): ").strip()

    # ถ้าไม่กรอกขนาดจอให้กำหนดเป็น 'ไม่ระบุ'
    if not screen_size:
        screen_size = "ไม่ระบุ"

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # อัปเดตข้อมูล
    entry["รายการ"] = item if item else entry["รายการ"]
    entry["s/n"] = serial_number if serial_number else entry["s/n"]
    entry["อาการ"] = symptom
    entry["ขนาดจอ"] = screen_size
    entry["วันที่และเวลาที่ตรวจ"] = timestamp

    # บันทึกข้อมูลลงไฟล์ JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"ข้อมูลของลำดับ {edit_index} ได้รับการอัปเดตเรียบร้อยแล้ว!")