# This class is used for check the robots.txt on a website.
# Check if we can scrap on a website target

from urllib import robotparser

robot_parser = robotparser.RobotFileParser()


# We read de robots.txt of the website
def prepare(robots_txt_url):
    # Sets the URL referring to a robots.txt file.
    robot_parser.set_url(robots_txt_url)
    # Reads the robots.txt URL and feeds it to the parser.
    robot_parser.read()


# Function that let us know if we can make scrap on a determinate URL
def is_allowed(target_url, user_agent='*'):
    # Returns True if the useragent is allowed to fetch the url.
    return robot_parser.can_fetch(user_agent, target_url)


if __name__ == '__main__':
    prepare('https://www.apress.com/robots.txt')
    print(is_allowed('https://www.apress.com/covers/'))
    print(is_allowed('https://www.apress.com/gp/python'))
