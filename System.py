from DB import DataBase
import numpy as np
import DB

class ManagementSystem:
    def __init__(self,route):
        self.text = DataBase(route)
        self.menu()

    def menu(self):
        self.array = np.array(self.text.DB,str)
        print("---도서 관리 시스템---")
        print("1.도서 추가")
        print("2.도서 검색")
        print("3.도서정보 수정")
        print("4.도서 삭제")
        print("5.현재 총 도서 목록 출력")
        print("6.저장")
        print("7.프로그램 나가기")
        self.option = int(input("메뉴를 선택하세요: "))
        if self.option == 1:
           self.add()
           self.menu()
        elif self.option == 2:
            self.search()
            self.menu()
        elif self.option == 3:
            self.changing()
            self.menu()
        elif self.option == 4:
            self.delete()
            self.menu()
        elif self.option == 5:
            self.booklist()
            self.menu()
        elif self.option == 6:
            self.save()
            self.menu()
        elif self.option == 7:
            self.save()

    def add(self):    # 도서추가
        self.bookname = input("추가할 도서명: ")
        self.author = input("저자: ")
        self.publicationyear = input("출판년도: ")
        self.publisher = input("출판사명: ")
        self.genre = input("장르: ")
        self.text.DB = np.append(self.text.DB, [[self.bookname,self.author,self.publicationyear,self.publisher,self.genre]], axis=0)
        print(self.text.DB)

    def search(self):    # 도서검색
        print("1.도서명 검색")
        print("2.저자 검색")
        print("3.출판년도 검색")
        print("4.출판사명 검색")
        print("5.장르 검색")
        
        self.option = int(input("검색할 방법을 선택하세요 : "))
        if self.option == 1:
            self.bookname = input("검색할 도서명: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.bookname)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.bookname],axis = 0)
                self.b = np.append(self.list1, [self.array[i][0]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])
                
        elif self.option == 2:
            self.author = input("검색할 저자: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.author)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.author],axis = 0)
                self.b = np.append(self.list1, [self.array[i][1]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 3:
            self.publicationyear = input("검색할 출판년도: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.publicationyear)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.publicationyear],axis = 0)
                self.b = np.append(self.list1, [self.array[i][2]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 4:
            self.publisher = input("검색할 출판사명: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.publisher)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.publisher],axis = 0)
                self.b = np.append(self.list1, [self.array[i][3]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])

        elif self.option == 5:
            self.genre = input("검색할 장르: ")
            self.array = np.array(self.text.DB,str)
            for i in range(len(self.text.genre)):
                self.list1 = []
                self.list2 = []
                self.a = np.append(self.list2,[self.genre],axis = 0)
                self.b = np.append(self.list1, [self.array[i][4]], axis=0)  
                if self.b[0] == self.a[0]:
                    print(self.array[i])

    def changing(self):    # 도서정보 수정
        print(self.array)
        self.change = int(input("[0:도서명,1:저자,2:출판년도,3:출판사,4:장르] 중 수정할 항목 선택 : "))
        if self.change == 0:
            self.num = int(input("수정할 책 번호(단, 첫줄부터 0) :"))    
            self.name = input("수정할 내용 : ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][0] = self.name
                    print(self.text.DB[i])
        elif self.change == 1:
            self.num = int(input("수정할 책 번호(단, 첫줄부터 0) :"))    
            self.name = input("수정할 내용 : ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][1] = self.name
                    print(self.text.DB[i])
        elif self.change == 2:
            self.num = int(input("수정할 책 번호(단, 첫줄부터 0) :"))    
            self.name = input("수정할 내용 : ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][2] = self.name
                    print(self.text.DB[i])
        elif self.change == 3:
            self.num = int(input("수정할 책 번호(단, 첫줄부터 0) :"))    
            self.name = input("수정할 내용 : ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][3] = self.name
                    print(self.text.DB[i])
        elif self.change == 4:
            self.num = int(input("수정할 책 번호(단, 첫줄부터 0) :"))    
            self.name = input("수정할 내용 : ")
            for i in range(len(self.text.DB)):
                if i == self.num:
                    self.text.DB[i][4] = self.name
                    print(self.text.DB[i])

    def delete(self):     # 도서삭제
        print(self.text.DB)
        self.tt = int(input("삭제할 책 번호(단, 첫줄부터 0) :"))
        for i in range(len(self.text.DB)):
            if i == self.tt:
               self.text.DB = np.delete(self.text.DB,(i),axis = 0) 
               print(self.text.DB)

    def booklist(self):    # 도서목록나열
        print(self.text.DB)
               
    def save(self):       # 저장
        np.save("C:/Users/junn7/eon/input.txt",self.text.DB)
        self.saveload = np.load("C:/Users/junn7/eon/input.txt.npy")
        print(self.saveload)

if __name__ =="__main__":
    MS = ManagementSystem("input.txt")