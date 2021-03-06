import os
import platform

global danhsachsv
danhsachsv = ["Blue","White","Black","Red"]

def show_menu():
    print("******************************************")
    print("(1)-Them Sinh Vien Moi Vao Danh Sach     *")
    print("(2)-Xoa Ten Sinh Vien Trong Danh Sach    *")
    print("(3)-Tim Ten Sinh Vien Trong Danh Sach    *")
    print("(4)-Xem Tat Ca Sinh Vien Trong Danh Sach *")
    print("(0)-Thoat                                *")
    print("******************************************")

def xemtatca():
    print("\n")
    print("************Danh Sach Sinh Vien***********")
    for tensinhvien in danhsachsv:
            print("-{}\t\t\t\t\t *".format(tensinhvien))
    print("******************************************")
            
def themsvmoi():
    print("\n")
    sinhvienmoi = (input("Nhap Ten Sinh Vien Muon Them: "))
    if sinhvienmoi in danhsachsv:
        print("{} Da Co Trong Danh Sach".format(sinhvienmoi))
    else:
        danhsachsv.append(sinhvienmoi)
        print("************Cap Nhat Danh Sach************")
        for tensinhvien in danhsachsv:
            print("-{}\t\t\t\t\t *".format(tensinhvien))
        print("******************************************")

def timtensv():
    print("\n")
    nhaptensvcantim = input("Nhap Ten Can Tim: ")
    if nhaptensvcantim in danhsachsv:
        print("{} Co Ten Trong Danh Sach".format(nhaptensvcantim))
    else:
        print("{} Khong Co Ten Trong Danh Sach".format(nhaptensvcantim))
    

def xoatensv():
    print("\n")
    xoatensv = input("Nhap Ten Muon Xoa: ")
    if xoatensv in danhsachsv:
        danhsachsv.remove(xoatensv)
        print("************Cap Nhat Danh Sach************")
        for tensinhvien in danhsachsv:
            print("-{}\t\t\t\t\t *".format(tensinhvien))
        print("******************************************")
    else:
        print("Khong Tim Thay {} Trong Danh Sach".format(xoatensv))

show_menu()

luachon = int(input("Nhap Lua Chon Cua Ban: "))

while luachon != 0:
    if luachon == 0:
        break
    elif luachon == 1:
        themsvmoi()
    elif luachon == 2:
        xoatensv()
    elif luachon == 3:
        timtensv()
    elif luachon == 4:
        xemtatca()
    else:
        print("Khong Co Lua Chon Nay")

    luachon = int(input("Nhap Lua Chon Cua Ban: "))


