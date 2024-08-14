import scrapy
from pathlib import Path
import pandas as pd


class TalentedgeSpider(scrapy.Spider):
    name = "talentedge"
    allowed_domains = ["talentedge.com"]
    start_urls = ["https://talentedge.com"]

    def start_requests(self):
        urls = [
            "https://talentedge.com/golden-gate-university/doctor-of-business-administration"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"talentedge-{page}.html"
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        courseLink = response.url
        title = response.css("h1::text").get()
        print(title)

        desc = response.css(".desc>p::text").getall()
        description = ""
        for des in desc:
            description += des + " "
        # print(description)

        duration = response.css(".duration-of-course>ul>li>p>strong::text").get().split(":")[-1]
        print(duration)

        timing = response.css(".duration-of-course>ul>li>p::text").get()
        print(timing)

        courseStart = response.css(".duration-of-course>ul>li>p>strong::text").getall()[1]
        print(courseStart)

        wh = response.css(".pl-deeper-undstnd to_flex_ul").get()
        # whatYouWill = ""
        # for sk in wh:
        #     whatYouWill += sk
        #     if(sk != wh[-1]):
        #         whatYouWill += " | "
        print(wh)

        skill = response.css(".key-skills-sec>ul>li::text").getall()
        skills = ""
        for sk in skill:
            skills += sk
            if(sk != skill[-1]):
                skills += " | "
        print(skills)

        targetStudent = response.css(".cs-content>h4::text").get().strip()
        # print(targetStudent)

        eligibility = response.css(".eligible-right-top-list>p::text").get()
        # print(eligibility)

        con = response.css(".sylab-tab-ul>ul>li>a::text").getall()
        i=0
        content = ""
        for c in con:
            content += c
        content = content.replace(' ', '')
        # print(content)

        instituteName = response.css(".about-ititle::text").get()
        print(instituteName)

        feeInInr = response.css(".program-details-total-pay-amt-right::text").get().replace(' ', '')
        print(feeInInr)

        faculty = response.css(".best-fname::text").getall()
        for i, name in enumerate(faculty, start=1):
            globals()[f'faculty_{i}_name'] = name.strip()
        
        # for i in range(1, len(faculty) + 1):
        #     variable_name = f'faculty_{i}_name'
        #     print(f"{globals()[variable_name]}")

        facultyDeg = response.css(".best-fdesingnation::text").getall()
        for i, name in enumerate(facultyDeg, start=1):
            globals()[f'faculty_{i}'] = name.strip()

        
        course_data = {
            "Course Link": courseLink,
            "Title": title,
            "Description":description,
            "Duration":duration,
            "Timing":timing,
            "Course Start":courseStart,
            "What you will":wh,
            "Skills":skills,
            "target students":targetStudent,
            "Prerequisites / Eligibility criteria":eligibility,
            "Content":content,
            "Faculty 1 Name":faculty_1_name,
            "Faculty 1":faculty_1,
            "Faculty 2 Name":faculty_2_name,
            "Faculty 2":faculty_2,
            "Faculty 3 Name":faculty_3_name,
            "Faculty 3":faculty_3,
            "Faculty 4 Name":faculty_4_name,
            "Faculty 4":faculty_4,
            "Faculty 5 Name":faculty_5_name,
            "Faculty 5":faculty_5,
            "Faculty 6 Name":faculty_6_name,
            "Faculty 6":faculty_6,
            "Faculty 7 Name":faculty_7_name,
            "Faculty 7":faculty_7,
            "Faculty 8 Name":faculty_8_name,
            "Faculty 8":faculty_8,
            "Faculty 9 Name":faculty_9_name,
            "Faculty 9":faculty_9,
            "Faculty 10 Name":faculty_10_name,
            "Faculty 10":faculty_10,
            "Institute Name":instituteName,
            "Fee in INR":feeInInr
        }

        data = []
        data.append(course_data)
        df = pd.DataFrame(data)

        df.to_excel('course_data.xlsx', index=False)



        


        




        
