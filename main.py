from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

movies = soup.find_all(name = "h3", class_ = "title")
years = soup.find_all(name="strong")
movie_titles = []
movie_years = []
for movie in movies:
    movie_text = movie.getText()
    movie_titles.append(movie_text)

# for movie_year in years:
#     movie_year = movie_year.getText()
#     movie_years.append(movie_year)


movie_titles = movie_titles[::-1]
# movie_years = movie_years[::-1]

# print(len(movie_titles))
# print(len(movie_years))


with open("movie_list.txt", 'w') as file:
    for x in range(len(movie_titles)):
         file.write(movie_titles[x])
         file.write(" ")
         # file.write(movie_years[x])
         file.write('\n')

# print(movie_text)