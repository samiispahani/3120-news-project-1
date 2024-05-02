 url = f"https://api.nytimes.com/svc/topstories/v2/{section}.json"
    params = {'api-key': api_key}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = [article['title'] for article in data['results']]
        return articles
    else:
        print("Failed to fetch articles:", response.status_code)
        return None

def main():
    api_key = '' 
    #Input the section you need
    section = input("Enter the section you want articles from (Technology, Politics): ").lower()

    articles = fetch_articles(api_key, section)
    if articles:
        print(f"Fetching articles from the {section} section...")
        print(f"Total Articles Fetched: {len(articles)}")
        
        keyword_counts = analyze_keywords(articles)
        
        print("\nKeyword Frequencies:")
        for keyword, count in keyword_counts.items():
            print(f"{keyword.capitalize()}: {count}")
        
      #Creates the histogram
        df = pd.DataFrame.from_dict(keyword_counts, orient='index', columns=['Frequency'])
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'Keyword'}, inplace=True)
        
        sns.barplot(x='Keyword', y='Frequency', data=df)
        plt.xticks(rotation=45)
        plt.title('Keyword Frequency Histogram')
        plt.show()
    else:
        print("No articles fetched.")

if __name__ == "__main__":
    main()
