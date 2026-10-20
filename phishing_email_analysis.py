import pandas as pd

def analyze_email(row):
text = (str(row["subject"]) + " " + str(row["body"])).lower()
score = 0

suspicious_words = [
"urgent",
"immediately",
"verify your account",
"blocked",
"password",
"won a prize",
"click this link"
]

for word in suspicious_words:
if word in text:
score += 1

if str(row["url"]).lower().startswith("http://"):
score += 1

if score >= 2:
return "Potential Phishing"
return "No Obvious Indicators"


emails = pd.read_csv("phishing_email_analysis.csv")
emails["result"] = emails.apply(analyze_email, axis=1)

emails.to_csv("phishing_email_analysis.csv", index=False)

emails[emails["result"] == "Potential Phishing"].to_csv(
"final_phishing_report.csv", index=False
)

print("Phishing email analysis completed successfully!")
print(emails["result"].value_counts())
