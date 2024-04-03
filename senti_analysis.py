from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
def analyze_sentiment(text):
    response = OpenAI(api_key=API_KEY).chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": "You are an expert in analyzing people's sentiments. I will provide you with sentences from a conversation, and I want you to determine their sentiment in few sentences"
            },
            {
                "role": "user",
                "content": "Hi, Joseph. I’m good. Yesterday went for a run. What about you?"
            },
            {
                "role": "assistant",
                "content": "The Speaker likes a sport. It seems he cares about his health’."
            },
            {
                "role": "user",
                "content": "Hello, today I will read a book, I like reading"
            },
            {
                "role": "assistant",
                "content": "The Speaker pretends to be smart"
            },
            {
                "role": "user",
                "content": "I will one day visit india, I have never been out of california"
            },
            {
                "role": "assistant",
                "content": "The Speaker pretends to want to travel to a different country"
            },
            {
                "role": "user",
                "content": "I have worked on k-means algorithm to classify data to a truth value provided"
            },
            {
                "role": "assistant",
                "content": "The Speaker is getting confused with unsupervised and supervised machine learning algorithms"
            },
            {
                "role": "user",
                "content": "I have worked on cloud engineering, like AWS, Kubernetes, docker and terraform"
            },
            {
                "role": "assistant",
                "content": "The Speaker is providing topics in cloud engineering and they are very vague about it"
            },
            {
                "role": "user",
                "content": "I have worked with SQL, in my previous company, I worked with storage procedures, views, grouping and CTE's to improvise the use of SQL in my work place"
            },
            {
                "role": "assistant",
                "content": "The Speaker is knowladgable on SQL, they seem confident in working with it"
            },
            {
                "role": "user",
                "content": f"{text}"
            }
        ],
        temperature=1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    sentiment = response.choices[0].message.content.strip()
    return sentiment

# if __name__ == "__main__":
#     # text = input("Enter the text to analyze: ")
#     text = "SPEAKER_1: Oh, my first impression were just notified to report to fort Dick's security, whether great many other young people being called from college students and high schools, and the impression was, of course, there was a new when the change existence. We were set by train to Georgia, where we were assigned to the of Battalion of which I spent the next two and a half years. The two ninety fourth Combat engineer Battalion. Well, with the invasion I was coming. We all knew, and we were training for it. The my battalion was sent to a marshal area in Wales. Where we were in prisons virtually for maybe two or three weeks preparing to be put on ships, we were loaded in two sections. We had the advanced section, and then the heavy equipment was going to come later. The advanced section with my railroad taken into Bristol. We've boarded the ship the Santa paula, which by then was known as the Susan B Anthony, it was a grace liner, and the we were put on the shipment and it was there that we were told that the actual invasion was about to take place and that we were going to land on d plus one, in support of the eighty second airborne division, which was landing, of course, in night before by and being dropped from the transport planes, So we were on the ship, sailing along the coast of England, Southern Coast. On d day as the landings are taking place we were prepared to dis dark from the Susan D Anthony, which we did do well we were who Have done that. Actually, we were preparing in in the bottom hole of the ship when the ship had a mine and started think. Therefore, we struggles to get from the bottom hole to the top hole and up to the deck. Which is the long process because there were lines of people in front of us. We were able to get out onto the deck. Where the skip of the ship was guiding us where to stand and moving whole batches the soldiers from one side of the ship together in an attempt to balance it, the ship eventually, went down. After we'd all got no"
#     sentiment = analyze_sentiment(text)
#     print(f"Speakers sentiment: {sentiment}")