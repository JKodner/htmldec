def html(fn):
    """HTML Tag"""
    def wrapped():
        return "<html>" + fn() + "</html>"
    return wrapped

def b(fn):
    """Bold Text"""
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def i(fn):
    """Italicized Test"""
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def u(fn):
    """Underline"""
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

def comment(fn):
    """HTML Comment"""
    def wrapped():
        return "<!--" + fn() + "-->"
    return wrapped

def body(fn):
    """HTML Body"""
    def wrapped():
        return "<body>" + fn() + "</body>"
    return wrapped

def h1(fn):
    """Heading (Size 1)"""
    def wrapped():
        return "<h1>" + fn() + "</h`>"
    return wrapped

def h2(fn):
    """Heading (Size 2)"""
    def wrapped():
        return "<h2>" + fn() + "</h2>"
    return wrapped

def h3(fn):
    """Heading (Size 3)"""
    def wrapped():
        return "<h3>" + fn() + "</h3>"
    return wrapped

def h4(fn):
    """Heading (Size 4)"""
    def wrapped():
        return "<h4>" + fn() + "</h4>"
    return wrapped

def h5(fn):
    """Heading (Size 5)"""
    def wrapped():
        return "<h5>" + fn() + "</h5>"
    return wrapped

def h6(fn):
    """Heading (Size 6)"""
    def wrapped():
        return "<h6>" + fn() + "</h6>"
    return wrapped

def p(fn):
    """Paragraph"""
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def div(fn):
    """Div"""
    def wrapped():
        return "<div>" + fn() + "</div>"

def head(fn):
    """HTML Head"""
    def wrapped():
        return "<head>" + fn() + "</head>"
    return wrapped

def form(fn):
    """User Input Form"""
    def wrapped():
        return "<form>" + fn() + "</head>"

def input(fn):
    """Form Input"""
    def wrapped():
        return "<input " + fn() + ">"
    return wrapped

def href(fn):
    """HTML Link"""
    def wrapped():
        return "<a href =" + fn() + "</a>"
    return wrapped

def img(fn):
    """HTML Image"""
    def wrapped():
        return "<img src=" + fn() + "</img>"
    return wrapped
def b(fn):
    """Bold Text"""
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def i(fn):
    """Italicized Test"""
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def comment(fn):
    """HTML Comment"""
    def wrapped():
        return "<!--" + fn() + "-->"
    return wrapped

def body(fn):
    """HTML Body"""
    def wrapped():
        return "<body>" + fn() + "</body>"
    return wrapped

def h1(fn):
    """Heading (Size 1)"""
    def wrapped():
        return "<h1>" + fn() + "</h`>"
    return wrapped

def h2(fn):
    """Heading (Size 2)"""
    def wrapped():
        return "<h2>" + fn() + "</h2>"
    return wrapped

def h3(fn):
    """Heading (Size 3)"""
    def wrapped():
        return "<h3>" + fn() + "</h3>"
    return wrapped

def h4(fn):
    """Heading (Size 4)"""
    def wrapped():
        return "<h4>" + fn() + "</h4>"
    return wrapped

def h5(fn):
    """Heading (Size 5)"""
    def wrapped():
        return "<h5>" + fn() + "</h5>"
    return wrapped

def h6(fn):
    """Heading (Size 6)"""
    def wrapped():
        return "<h6>" + fn() + "</h6>"
    return wrapped

def p(fn):
    """Paragraph"""
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def div(fn):
    """Div"""
    def wrapped():
        return "<div>" + fn() + "</div>"

def head(fn):
    """HTML Head"""
    def wrapped():
        return "<head>" + fn() + "</head>"
    return wrapped

def form(fn):
    """User Input Form"""
    def wrapped():
        return "<form>" + fn() + "</head>"

def href(fn):
    """HTML Link"""
    def wrapped():
        return "<a href =" + fn() + "</a>"
    return wrapped

def img(fn):
    """HTML Image"""
    def wrapped():
        return "<img src=" + fn() + "</img>"
    return wrapped

def table(fn):
    """Table"""
    def wrapped():
        return "<table>" + fn() + "</table>"
    return wrapped

def tbody(fn):
    """Table Body"""
    def wrapped():
        return "<tbody>" + fn() + "</tbody>"
    return wrapped

def td(fn):
    """Table Data"""
    def wrapped():
        return "<td>" + fn() + "</td>"
    return wrapped

def tr(fn):
    """Table Row"""
    def wrapped():
        return "<tr>" + fn() + "</tr>"
    return wrapped

def thead(fn):
    """Table Head"""
    def wrapped():
        return "<thead>" + fn() + "</thead>"
    return wrapped

def ol(fn):
    """Ordered List"""
    def wrapped():
        return "<ol>" + fn() + "</ol>"
    return wrapped

def ul(fn):
    """Table"""
    def wrapped():
        return "<ul>" + fn() + "</ul>"
    return wrapped

def li(fn):
    """List Item"""
    def wrapped():
        return "<li>" + fn() + "</li>"
    return wrapped

def span(fn):
    """Span"""
    def wrapped():
        return "<span>" + fn() + "</span>"
    return wrapped

def style(fn):
    """Table"""
    def wrapped():
        return "<style>" + fn() + "</style>"
    return wrapped

def ul(fn):
    """Table"""
    def wrapped():
        return "<ul>" + fn() + "</ul>"
    return wrapped