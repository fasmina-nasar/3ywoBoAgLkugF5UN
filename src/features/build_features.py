class Preprocess:
    def preprocess_texts(self, df):
        
        # cleaning 'location' column         
        df['location'] = df['location'].apply(lambda x: re.sub('Kanada', 'canada', x))
        df['location'] = df['location'].apply(lambda x: re.sub('Türkiye', 'Turkey', x))
        df['location'] = df['location'].apply(lambda x: re.sub('Amerika Birleşik Devletleri','United States of America', x))
        
        # cleaning 'job_title' column
        df['job_title'] = df['job_title'].apply(lambda x: re.sub(r'HR', 'Human Resources', x))  # replace HR by Human Resources
        df['job_title'] = df['job_title'].apply(lambda x: re.sub(r'\d+',"",x)) # remove digits
        df['job_title'] = df['job_title'].replace('[^\w\s]+', "", regex=True)   # remove punctuations       
        df['job_title'] = df['job_title'].str.lower()   # transfrom into lowercase letters
        
        # cleaning 'connection' column
        df['connection'] = df['connection'].str.replace('+','')    # remove '+'
        df['connection'] = df['connection'].astype(int)  # convert dtype of connection into integer
    
        return df
    
    def text_lemmatization(self, text):
        
        # tokenize the text
        tokens = word_tokenize(text)
        
        # remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]
        
        # perform lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        
        # return processed text as a single token
        return ' '.join(tokens)