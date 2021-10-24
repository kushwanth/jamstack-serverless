import smtplib, ssl, os
import azure.functions as func

def send_email(data):
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = os.getenv("senderemail")
    receiver_email = os.getenv("recieveremail")
    password = os.getenv("password")
    ssl_context = ssl.create_default_context()
    try:
        email_server = smtplib.SMTP_SSL(smtp_server, port, context=ssl_context)
        email_server.login(sender_email, password)
        msg = "Subject: New Review from "+data["name"]+"\n Review for : "+data["title"]+"\n"+data["content"]
        email_server.sendmail(sender_email, receiver_email, msg)
        return True
    except Exception as e:
        return False
    finally:
        email_server.quit()

def main(req: func.HttpRequest) -> func.HttpResponse:
    res = "Emailing!!!"
    try:
        review = req.get_json()
        email_status = send_email(review)
        if(email_status is True):
            res = "Mail sent Successfully"
        else:
            res = "Error: Unable to send Email"
    except Exception as e:
        print(e)
        res = "Server Error"
    return func.HttpResponse(res)
