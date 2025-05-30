# Name: Ivan Maldonado
# Date: May 6, 2025
# Description: This script stores a dictionary of authors and the years they died. It then loops through the collection and prints messages like:



# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889",
}

for author, date in authors.items():
    print(f"{author} died in {date}.")

