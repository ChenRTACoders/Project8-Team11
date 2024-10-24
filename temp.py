# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
#11组余锦杉 杨益 刘书源
ticket_data = []

def add_ticket_info():
    ticket_type = input("请输入票种：")
    price = float(input("请输入价格："))
    purchase_date = input("请输入购票日期：")
    passenger_name = input("请输入乘客姓名：")
    ticket_data.append((ticket_type, price, purchase_date, passenger_name))

def generate_report():
    import datetime
    report_date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(f"票务统计报告 - 生成日期：{report_date}")
    unique_ticket_types = set([data[0] for data in ticket_data])
    for ticket_type in unique_ticket_types:
        total_sales = 0
        quantity = 0
        for data in ticket_data:
            if data[0] == ticket_type:
                total_sales += data[1]
                quantity += 1
        print(f"票种：{ticket_type}，销售数量：{quantity}，总收入：{total_sales}")

while True:
    choice = input("请选择操作：1.添加票务信息；2.生成报告；3.退出。")
    if choice == '1':
        add_ticket_info()
    elif choice == '2':
        generate_report()
    elif choice == '3':
        break
    else:
        print("无效选择，请重新输入。")

