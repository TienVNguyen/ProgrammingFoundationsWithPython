import webbrowser

class Movie():
    def __init__(self, m_title, m_storylife, m_poster_image_url, m_trailer_youtube_url):
        self.title = m_title
        self.storylife = m_storylife
        self.poster_image_url = m_poster_image_url
        self.trailer_youtube_url = m_trailer_youtube_url
        
    def show_trailer(self):
        webbrowser.open_new_tab(self.trailer_youtube_url)
        webbrowser.open_new(self.trailer_youtube_url)       
