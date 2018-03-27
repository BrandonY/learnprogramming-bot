import praw

def main():
    # Note - a praw.ini file defining reddit credentials for 'Robot' must exist.
    reddit = praw.Reddit('robot')
    monitoring_user = reddit.redditor('Username')

    subreddit = reddit.subreddit('learnprogramming')
    for submission in subreddit.stream.submissions():
        if submission.title[0] == 'H':
            print('Found message')
            message = ('Found a submission beginning with H.\n\nURL: {}\n\n{}'
                .format(
                    submission.title,
                    submission.url,
                    submission.selftext[:25]))
            monitoring_user.message('Submission found', message)
        else :
            print('Filtered out submission {}'.format(submission.title))

if __name__ == '__main__':
    main()
