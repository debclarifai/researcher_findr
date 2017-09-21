import subprocess

def run_scrape(list_of_keywords):
    authors_to_search = {}
    for keyword in list_of_keywords:
        bashCommand = "python scholar.py -A " + keyword + " -c 10 --citation=en"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()   
        authors = parse_output(keyword, output)
        authors_to_search[keyword] = authors
    return authors_to_search

def parse_output(keyword, output):
    articles = output.split('\n\n')
    authors = []
    for article in articles:
        authors_pre_processed = article.split("%A ")
        num_authors = len(authors_pre_processed)
        for i, author in enumerate(authors_pre_processed):
            # ignore the first and last indices as they are not authors
            if i == 0:
                continue
            # the last index needs to further process
            if i == num_authors - 1:
                last_author = author.split("%")
                author = last_author[0]
                author = author[:-4]
                authors.append(author)
                break
            author = author[:-4]
            authors.append(author)
    return authors

def main():
    user_input = raw_input("Input keywords:(delimited by ;) ")
    list_of_keywords = user_input.split(";")
    return run_scrape(list_of_keywords)

main()