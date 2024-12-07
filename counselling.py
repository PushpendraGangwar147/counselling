# Load data from CSV
import csv
def load_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Filter institutes based on user preferences
def filter_institutes(data, user_rank, user_category, user_gender):
    user_rank=int(user_rank)
    filtered_data = []
    for row in data:
          try:
            if row['Closing']=='':
                continue
            cutoff_rank =int(row['Closing'])
            if user_rank <= cutoff_rank+0.15*cutoff_rank and user_rank >= cutoff_rank-0.15*cutoff_rank:
                if (user_gender=="Female"):
                    if((row['Category']==user_category) or row['Category']=='OPEN'):
                        filtered_data.append(row)
                elif(row['Gender']=="Neutral"):
                    if((row['Category']==user_category)or row['Category']=='OPEN'):
                        filtered_data.append(row)
                

          except :
              continue

    for row in filtered_data:
            a=int(row['Closing'])
            percent=((a-1000)/a)*100
            if percent>=8:
                row['Chances']="High"
            elif (percent < 8) and (percent >=0):
                row['Chances']="Moderate"
            else:
                row['Chances']="Low"  
    return filtered_data

# # Example usage
# data = load_data('E:\\python\counselling\\josaa2.csv')
# user_rank = 200
# user_category = "OPEN"
# user_gender = "Female"

# filtered_results = filter_institutes(data, user_rank, user_category, user_gender)
# for row in filtered_results:
#     print(row['Institue'])
#     print(row['Closing'])
#     print(row['Gender'])
#     print(row['Category'])
#     print(row['Branch'])
#     a=int(row['Closing'])
#     percent=((a-user_rank)/a)*100
#     if percent>=8:
#         print('high')
#     elif (percent < 8) and (percent >=0):
#         print("moderate")
#     else:
#         print("low")


# def dashboard():
#     print("Welcome to Counselling Era\n")   
#     print("(1) Sign Up")
#     print("(2) Login")
#     print("(3) Know about Counselling Era")
#     print("(4) How to use ?")
#     print("(5) Exit\n")
#     op=int(input("Choose an option : "))
#     return op
# op=dashboard()

# def sub_category():
#      print("(1) Armed Forces")
#      print("(2) Freedom Fighter")
#      print("(3) PWD")
#      s_category=int(input("Enter Your Sub Category"))
#      return s_category

# def uptac(data_csv):
#      data = load_data(data_csv)
#      user_rank=int(input('Enter your Rank : '))
#      print("(1) Male")
#      print("(2) Female")
#      gender=int(input("Choose your Gender : "))
#      print("(1) OPEN")
#      print("(2) OBC")
#      print("(3) EWS")
#      print("(4) SC")
#      print("(5) ST")
#      print("(6) OPEN(Fee Waiver)")
#      category=int(input("Choose your Category : "))
#      print("")

#      if   category==1:
#           x=sub_category()
#           if x==1:
#                user_category='OPEN(AF)'
#           elif x==2:
#                user_category='OPEN(FF)'
#           elif x==3:
#                user_category='OPEN(PH)'
#      elif category==2:
#           x=sub_category()
#           if x==1:
#                user_category='OPEN(TF)'
#           elif category==3:
#                user_category='OPEN(GIRL)'
#           elif category==4:
#                user_category='OPEN(AF)'
#           elif category==5:

#                user_category='OPEN'
#      elif category==2:
#           user_category='BC'
#      elif category==3:
#           user_category='EWS'
#      elif category==4:
#           user_category='SC'
#      elif category==5:
#           user_category='ST'
     
#      print("")
#      print("")
#      print("")
#      print("")
#      print("")

     
     
#      s_category=int(input("Enter Your Sub-Category : "))
#      print("")
#      if category==1:
#           user_category='SC(AF)'
#      elif category==2:
#           user_category='OPEN(TF)'
#      elif category==3:
#           user_category='OPEN(GIRL)'
#      elif category==4:
#           user_category='OPEN(AF)'
#      elif category==5:
#           user_category='BC(GIRL)'
#      elif category==11:
#           user_category='EWS(GL)'
#      elif category==12:
#           user_category='EWS(OPEN)'
#      elif category==13:
#           user_category='BC(AF)'
#      elif category==14:
#           user_category='SC(GIRL)'
#      elif category==15:
#           user_category='ST(GIRL)'
#      elif category==16:
#           user_category='EWS(AF)'
#      elif category==17:
#           user_category='OPEN(FF)'
#      elif category==18:
#           user_category='BC(FF)'
#      elif category==19:
#           user_category='OPEN(PH)'
#      elif category==20:
#           user_category='BC(PH)'
#      elif category==21:
#           user_category='SC(FF)'
#      elif category==22:
#           user_category='SC(PH)'
#      elif category==23:
#           user_category='EWS(PH)'
#      elif category==24:
#           user_category='EWS(FF)'
#      if gender==1:
#           user_gender='Male'
#      elif gender==2:
#           user_gender='Female'
#      filtered_results = filter_institutes(data, user_rank, user_category, user_gender)
#      for row in filtered_results:
#             print(row['Institue'])
#             print("Branch:-",row['Branch'])
#             print("Closing Rank(2024):-",row['Closing'],end=", " )
#             print("Gender:-",row['Gender'],end=", ")
#             print("Category:-",row['Category'],end=", ")
#             print("Quota:-",row['Quota'],end=", ")
#             a=int(row['Closing'])
#             percent=((a-user_rank)/a)*100
#             if percent>=8:
#                 print("Possibility:- High")
#             elif (percent < 8) and (percent >=0):
#                 print("Possibility:- Moderate")
#             else:
#                 print("Possibility:- Low")
#             print("*" * 130)



def counselling_info (op2,rank,category,gender):
     # print("(1) : JoSAA")
     # print("(2) : CSAB")
     # print("(3) : UPTAC")
     if op2=='JoSAA':
          data_csv='josaa2.csv'
     elif op2=='UPTAC':
          data_csv='uptac.csv'
     elif op2=='CSAB':
          data_csv='csab.csv'
          # uptac(data_csv)
     data = load_data(data_csv)
     # user_rank=int(input('Enter your Rank : '))
     # print("(1) Male")
     # print("(2) Female")
     # gender=int(input("Choose your Gender : "))
     # print("(1) OPEN")
     # print("(2) OBC-NCL")
     # print("(3) EWS")
     # print("(4) SC")
     # print("(5) ST")
     # category=int(input("Choose your Category : "))
     # print("")
     # if category==1:
     #      user_category='OPEN'
     # elif category==2:
     #      user_category='OBC-NCL'
     # elif category==3:
     #      user_category='EWS'
     # elif category==4:
     #      user_category='SC'
     # elif category==5:
     #      user_category='ST'
     # if gender==1:
     #      user_gender='Male'
     # elif gender==2:
     #      user_gender='Female'
     return filter_institutes(data, rank, category, gender)

# if(op==1):
#     name=input("Enter your Name : ")
#     mob=input("Enter your Mob.No. : ")
#     stream=input("Enter your stram : ")
#     user_id=input("Create your User id : ")
#     pswd=input("Create a strong password : ")
#     with open("E:\\python\\counselling\\data.csv",'a',newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([name,mob,stream,user_id,pswd])

# if(op==2):
#     id=input("Enter your User I'd : ")
#     paswd=input("Enter your Password : ")
#     with open("E:\\python\\counselling\\data.csv","r") as file:
#         reader = csv.reader(file)
#         for row in reader :
#             if(row[3]==id and row[4]==paswd):
#                 print("Logged in Successfully")
#                 #print(row)
#                 op2=counselling_info()
                
#                 if(op2==1):
#                      counselling_info ()

#                 break
#         else:
#                 print("Wrong User I'd or Password")       


















