'''
1. Product Review Analysis
Objective:
The aim of this assignment is to extract insights from product reviews by using string manipulation 
to categorize and summarize customer feedback for a SaaS product.

Task 1: Keyword Highlighter

Write a program that searches through a series of product reviews for keywords such as 
"good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. Use a predefined 
list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.
'''
# i need to find the word first with a for loop in another for loop.
# i need to use .replace() so that i can change the word with another within the review.

# Task one

review = ["good", "excellent", "bad", "poor", "average"]
comments = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


for  c in comments:
    for r in review:
        result = c.find(r)
        if result == -1:
            pass
        else:
            new_comment = c.replace(r,r.upper())
            print(new_comment)


# Task two 


comments = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]


def review_counter(comments):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "like"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "worst"] 
    positive_counter = 0
    negative_counter = 0 
    for count, c in enumerate(comments):
        for p in positive_words:
            result_p = c.count(p)
            if result_p == -1:
                pass
            elif result_p == True:
                positive_counter +=1
      
        for n in negative_words:
            result_n = c.count(n)
            if result_n == -1:
                pass
            elif result_n == True:
                negative_counter +=1
    else:
        return f"We had {positive_counter} positive reviews and {negative_counter} negative reviews out of {count} reviews total on this product!\nThat is a {(positive_counter / count) * 100:.2f}% positive feed back on this product."
                
                    
while True:
    user_input = input("Do you want to [V]iew, [A]dd, or [E]xit").upper()
    if user_input == "E":
        break
    elif user_input == "V":
        print(review_counter(comments))
    elif user_input == "A":
        new_comments = input("Please enter in the comment that you would like the add: ")
        capitalize_new_comment = str.capitalize(new_comments)
        comments.append(capitalize_new_comment)
    else:
        print("Invalid input!")







# Task three
    

comments = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]


def review_counter(comments):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing", "like"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar", "worst"] 
    positive_counter = 0
    negative_counter = 0 
    for count, c in enumerate(comments):
        for p in positive_words:
            result_p = c.count(p)
            if result_p == -1:
                pass
            elif result_p == True:
                positive_counter +=1
      
        for n in negative_words:
            result_n = c.count(n)
            if result_n == -1:
                pass
            elif result_n == True:
                negative_counter +=1
    else:
        return f"We had {positive_counter} positive reviews and {negative_counter} negative reviews out of {count} reviews total on this product!\nThat is a {(positive_counter / count) * 100:.2f}% positive feed back on this product.\n"



def comments_shortened(comments, max_length=30):
    words = c.strip().split()
    summary = ""
    for word in words:
        if len(summary) + len(word) + 1 <= max_length:
            summary += word + " "
        else:
            break
    if len(summary) < len(c):
        summary = summary.rstrip() + " ..."
    return f"The new comment is: {summary}\nThe old comment was: {c}\n"


  
while True:
    user_input = input("Do you want to [V]iew, [A]dd, or [E]xit ").upper()
    if user_input == "E":
        break
    elif user_input == "V":
        print(review_counter(comments))
        
        for count, c in enumerate(comments):
            print(f"{count +1}. {comments_shortened(c)}")
    elif user_input == "A":
        new_comments = input("Please enter in the comment that you would like the add: ")
        capitalize_new_comment = str.capitalize(new_comments)
        comments.append(capitalize_new_comment)
    else:
        print("Invalid input!")





