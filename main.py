import crawler as c
import yaml

## load info.yaml
with open('resource/info.yaml') as f:
    info = yaml.load(f)

if "__main__" == __name__:
    print("================== start ===============")
    url = 'https://www.bbc.com/sport/football/premier-league/top-scorers'
    crawler = c.Crawler(url)
    crawler.doCrawling()

    apiUrl = info["apiUrl"]
    print(crawler.reqAPI(apiUrl))
    print("=================== end ================")