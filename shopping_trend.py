import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load the data
df = pd.read_csv('shopping_trends_updated1.csv')
df.to_excel('shopping_trends_updated1.xlsx')                        #converts to excel file

print("Overview of the document.")
print(df.head())                                                   #only the top few rows are shown
print("Rows and Columns in the file : ", df.shape)                                                   #gives us the total number of rows and columns 
print("Number of null values:\n", df.isnull().sum())                                            #finds number of null values in each column

#Gives us unique values of all columns 
print("The unique values of the 'Gender' column are:",  df['Gender'].unique())
print()# This will print a blank line
print("The unique values of the 'Category' column are:", df['Category'].unique())
print() 
print("The unique values of the 'Size' column are: " , df['Size'].unique())
print()
print("The unique values of the 'Subscription Status' column are: ", df['Subscription Status'].unique())
print()
print("The unique values of the 'Shipping Type' column are: " , df['Shipping Type'].unique())
print()
print("The unique values of the 'Discount Applied' column are: ", df['Discount Applied'].unique())
print()
print("The unique values of the 'Promo Code Used' column are: ",  df['Promo Code Used'].unique())
print()
print("The unique values of the 'Payment Method' column are: ", df['Payment Method'].unique())



#OBSERVATION :
'''
The dataset consists of 3900 rows and 18 columns, representing a comprehensive collection of customer shopping behavior. It is clean and complete, with no null values, allowing us for smooth and confident analysis. Below is a summary of the columns and their significance:

1.Customer ID: Unique identifier for each customer, facilitating individual-level analysis.
2.Age: Helps assess age demographics and their influence on preferences and behavior.
3.Gender: Enables the study of buying patterns based on gender differences.
4.Item Purchased: Details specific products purchased, aiding in identifying popular items.
5.Category: Groups products (e.g., clothing, footwear) for trend analysis within categories.
6.Purchase Amount (USD): Reveals spending habits and customer segments based on expenditure.
7.Location: Provides geographical insights, highlighting regional preferences.
8.Size: Tracks size preferences, important for inventory and sales strategies.
9.Color: Analyzes customer color preferences and their influence on purchases.
10.Season: Explores seasonal trends and their impact on buying behavior.
11.Review Rating: Offers customer satisfaction feedback and quality insights.
12.Subscription Status: Indicates customer loyalty and engagement levels.
13.Shipping Type: Highlights preferred delivery methods among customers.
14.Discount Applied: Examines the effect of discounts on purchase decisions.
15.Promo Code Used: Evaluates promotional campaign effectiveness.
16.Previous Purchases: Tracks customer loyalty and repeat buying behavior.
17.Payment Method: Identifies favored payment methods for transactions.
18.Frequency of Purchases: Provides insights into customer buying habits over time.
'''

#1.	What is the overall distribution of customer ages in the dataset?
def age_distribution(df):
    print(df['Age'].value_counts())

    plt.hist(df['Age'])
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Customer ages')
    plt.show()


#2.	How does the average purchase amount vary across different product categories?
def average_purchase(df):
    avg_purchase = df.groupby('Category')['Purchase Amount (USD)'].mean()
    print(avg_purchase) 

    plt.figure(figsize=(10,6))
    avg_purchase.plot(kind='bar')
    plt.title('Purchase across different categories')
    plt.xlabel('Category')
    plt.ylabel('Purchase Amount (USD)')
    plt.show()

#3.	Which gender has the highest number of purchases?
def highest_purchase_by_gender(df):
    gender_count = df['Gender'].value_counts()
    print(gender_count)

    plt.figure(figsize=(10,6))
    gender_count.plot(kind='bar')
    plt.title('Purchases by Male and Female')
    plt.xlabel('Gender')
    plt.ylabel('Number of Purchases')
    plt.show()

#4.	What are the most commonly purchased items in each category?
def commonly_purchased_items(df):
    commonly_purchased = df.groupby('Category')['Item Purchased'].value_counts()
    print(commonly_purchased)

    plt.figure(figsize=(15,10))
    commonly_purchased.plot(kind='bar')
    plt.title('Commonly Purchased Amount in each category')
    plt.xlabel('Category')
    plt.ylabel('Number of purchases')
    plt.show()

#5.	Are there any specific seasons or months where customer spending is significantly higher?
def spending_by_season(df):
    seasons = df['Season'].value_counts()
    print(seasons)

    seasons.plot(kind = 'bar', color = 'blue')
    plt.xlabel('Seasons')
    plt.ylabel('Number of purchases')
    plt.show()


#6.	What is the average rating given by customers for each product category?
def average_rating_by_customer(df):
    avg_rating = df.groupby('Category')['Review Rating'].mean()
    print(avg_rating)

    plt.figure(figsize=(10,6))
    avg_rating.plot(kind='bar')
    plt.title('Average Rating by Customer for each product')
    plt.xlabel('Category')
    plt.ylabel('Review Rating')
    plt.show()


#7.	Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?
def purchase_behaviour_by_subscription(df):
    subscribed_vs_non_subscribed = df.groupby('Subscription Status')['Purchase Amount (USD)'].agg(['mean', 'count'])
    print(subscribed_vs_non_subscribed)

    subscribed_vs_non_subscribed['mean'].plot(kind='bar')
    plt.title('Average Purchase Amount')
    plt.xlabel('Subscription Status')
    plt.ylabel('Avg. Purchase Amount')
    plt.show()

    subscribed_vs_non_subscribed['count'].plot(kind = 'bar')
    plt.title('Number of purchases')
    plt.xlabel('Subscription Status')
    plt.ylabel('Number of Purchases')
    plt.show()

#8.	Which payment method is the most popular among customers?
def popular_payment_method(df):
    payment_method = df['Payment Method'].value_counts()
    print(payment_method)

    payment_method.plot(kind='bar')
    plt.title('Popular Payment Methods')
    plt.xlabel('Payment Method')
    plt.ylabel('Number of payments')
    plt.show()

#9.	Do customers who use promo codes tend to spend more than those who don't?
def effect_of_promo_code(df):
    promo_code = df.groupby('Promo Code Used')['Purchase Amount (USD)'].sum()
    print(promo_code)
    plt.figure(figsize=(10,6))
    promo_code.plot(kind='bar')
    plt.title('Promo code')
    plt.ylabel('Number of customers')
    plt.show()

#10.	How does the frequency of purchases vary across different age groups?
def frequency_of_purchase_across_agegroups(df):
    age_bins = [0,18,25,35,45,55,65,100]
    age_labels = ['0-18', '19-25','26-35','36-45','46-55','56-65','66-100']
    df['AgeGroup'] = pd.cut(df['Age'], bins = age_bins, labels=age_labels, right=True)

    age_group_purchase = df['AgeGroup'].value_counts().sort_index()
    print(age_group_purchase)

    plt.figure(figsize=(10,6))
    age_group_purchase.plot(kind='bar')
    plt.title('Purchases according to age groups')
    plt.xlabel('Ages')
    plt.ylabel('Purchase Amount')
    plt.show()

#11.	Are there any correlations between the size of the product and the purchase amount?
def relation_between_size_and_purchase_amount(df):
    size_purchase_amount = df.groupby('Size')['Purchase Amount (USD)'].sum()
    print(size_purchase_amount)

    plt.figure(figsize=(10,6))
    size_purchase_amount.plot(kind='bar')
    plt.title('Total amount by product size')
    plt.xlabel('Sizes')
    plt.ylabel('Purchase Amount')
    plt.show()

#12.	Which shipping type is preferred by customers for different product categories?
def shipping_type_different_categories(df):
    shipping_type = df.groupby('Category')['Shipping Type'].value_counts()
    print(shipping_type)

    plt.figure(figsize=(15,15))
    shipping_type.plot(kind='bar')
    plt.title('Shipping Type by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Number of Customers')
    plt.show()


#13.	How does the presence of a discount affect the purchase decision of customers?
def effect_of_discount(df):
    discount = df.groupby('Discount Applied')['Purchase Amount (USD)'].agg(['sum','count'])
    print(discount)

    #effect of discount on purchase amount
    plt.figure(figsize=(10,6))
    discount['sum'].plot(kind='bar')
    plt.title('Total Purchase Amount: Discount Applied vs Not Applied')
    plt.xlabel('Discount Applied')
    plt.ylabel('Total Purchase Amount (USD)')
    plt.show()

    #effect of discount on number of purchase
    plt.figure(figsize=(10,6))
    discount['count'].plot(kind='bar')
    plt.title('Number of purchases : Discount vs No Discount')
    plt.xlabel('Discount Applied')
    plt.ylabel('Number of purchases')
    plt.show() 


#14.	Are there any specific colors that are more popular among customers?
def popular_colors(df):
    color = df['Color'].value_counts()
    print(color)

    color.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Popularity of Colors ')
    plt.ylabel('')
    plt.show()


#15.	What is the average number of previous purchases made by customers?
def average_previous_purchases(df):
    avg_previous_purchase = df['Previous Purchases'].mean()
    print(avg_previous_purchase)

    plt.figure(figsize=(16,8))
    df['Previous Purchases'].plot(kind='hist')
    plt.title('Average number of previous purchase')
    plt.xlabel('Previous Purchases')
    plt.ylabel('Frequency')
    plt.show()



#16.	How does the purchase amount differ based on the review ratings given by customers?
def purchase_amount_by_review_rating(df):
    purchase_review = df.groupby('Review Rating')['Purchase Amount (USD)'].mean()
    print(purchase_review)
    plt.figure(figsize=(10, 6))
    purchase_review.plot(kind='bar')
    plt.title('Average Purchase Amount by Review Rating')
    plt.xlabel('Review Rating')
    plt.ylabel('Average Purchase Amount (USD)')
    plt.show()


#17.	Are there any noticeable differences in purchase behavior between different locations?
def diff_purchase_behaviour_between_locations(df):
    location_purchase_behavior = df.groupby('Location')['Purchase Amount (USD)'].agg(['sum', 'count', 'mean'])
    print(location_purchase_behavior)

    # Plot the total purchase amount by location
    plt.figure(figsize=(12, 6))
    location_purchase_behavior['sum'].plot(kind='bar', color='green')
    plt.title('Total Purchase Amount by Location')
    plt.xlabel('Location')
    plt.ylabel('Total Purchase Amount (USD)')
    plt.show()

    # Plot the number of purchases by location
    plt.figure(figsize=(12, 6))
    location_purchase_behavior['count'].plot(kind='bar', color='blue')
    plt.title('Number of Purchases by Location')
    plt.xlabel('Location')
    plt.ylabel('Number of Purchases')
    plt.show()

    # Plot the average purchase amount by location
    plt.figure(figsize=(12, 6))
    location_purchase_behavior['mean'].plot(kind='bar', color='orange')
    plt.title('Average Purchase Amount by Location')
    plt.xlabel('Location')
    plt.ylabel('Average Purchase Amount (USD)')
    plt.show()


#18. Is there a relationship between customer age and the category of products they purchase?
def age_and_category(df):
    age_bins = [0,18,25,35,45,55,65,100]
    age_labels = ['0-18', '19-25','26-35','36-45','46-55','56-65','66-100']
    df['AgeGroup'] = pd.cut(df['Age'], bins = age_bins, labels=age_labels, right=True)

    age_category_crosstab = pd.crosstab(df['AgeGroup'], df['Category'])
    print(age_category_crosstab)


    # Plot the crosstab as a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(age_category_crosstab, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Relationship Between Customer Age and Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Age Group')
    plt.show()


#19.	How does the average purchase amount differ between male and female customers?
def diff_between_male_and_female_purchase_amount(df):
    purchase_gender = df.groupby('Gender')['Purchase Amount (USD)'].agg(['mean','count'])
    print(purchase_gender)

    plt.figure(figsize=(10,6))
    purchase_gender.plot(kind='bar')
    plt.title('Average Purchase Amount by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Purchase Amount')
    plt.show()

def main():
    while True:
        print("""
    Please choose an analysis to perform:
    1. Overall distribution of customer ages
    2. Average purchase amount across different product categories
    3. Gender with the highest number of purchases
    4. Most commonly purchased items in each category
    5. Customer spending by season
    6. Average rating given by customers for each product category
    7. Differences in purchase behavior between subscribed and non-subscribed customers
    8. Most popular payment method among customers
    9. Effect of promo codes on spending
    10. Frequency of purchases across different age groups
    11. Correlation between product size and purchase amount
    12. Preferred shipping type by product category
    13. Effect of discounts on purchase decisions
    14. Popularity of specific colors among customers
    15. Average number of previous purchases made by customers
    16. Purchase amount based on review ratings
    17. Differences in purchase behavior between different locations
    18. Relationship between customer age and product category
    19. Average purchase amount by gender
    """)
        choice = input("Choose an analysis to perform (1-19): ")
        if choice == "1":
            age_distribution(df)
        elif choice == "2":
            average_purchase(df)
        elif choice == "3":
            highest_purchase_by_gender(df)
        elif choice == "4":
            commonly_purchased_items(df)
        elif choice == "5":
            spending_by_season(df)
        elif choice == "6":
            average_rating_by_customer(df)
        elif choice == "7":
            purchase_behaviour_by_subscription(df)
        elif choice == "8":
            popular_payment_method(df)
        elif choice == "9":
            effect_of_promo_code(df)
        elif choice == "10":
            frequency_of_purchase_across_agegroups(df)
        elif choice == "11":
            relation_between_size_and_purchase_amount(df)
        elif choice == "12":
            shipping_type_different_categories(df)
        elif choice == "13":
            effect_of_discount(df)
        elif choice == "14":
            popular_colors(df)
        elif choice == "15":
            average_previous_purchases(df)
        elif choice == "16":
            purchase_amount_by_review_rating(df)
        elif choice == "17":
            diff_purchase_behaviour_between_locations(df)
        elif choice == "18":
            age_and_category(df)
        elif choice == "19":
            diff_between_male_and_female_purchase_amount(df)
        else:
            print("Invalid choice.")
            continue

        while True:
            option = input("Do you want to continue (y/n? ").lower()
            if(option == 'y'):
                break
            elif(option == 'n'):
                print("Goodbye.")
                return
            else:
                print("Invalid option")

if __name__ == "__main__":
    main()