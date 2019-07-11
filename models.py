import string
from random import randint, choice

from werkzeug.security import generate_password_hash


# Todo shove this somewhere else, in a controllers or utils
def create_strong_password():
    # Generate a random secure password to be inserted
    password = ""
    #   Special characters array
    SpecialChar = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "&",
        "*",
        "(",
        ")",
        "_",
        "+",
        "=",
        "[",
        "{",
        "]",
        "}",
        "~",
        ">",
        "<",
        "|",
        "?",
        "/",
    ]
    #   Create a password with 8 characters
    for i in range(2):
        # pic a uppercase char
        password = password + choice(string.ascii_uppercase)
        # pic a lowercase char
        password = password + choice(string.ascii_lowercase)
        # pic a random number
        password = password + str(randint(0, 9))
        # pic a special char in the array
        password = password + choice(SpecialChar)
    return password


class User:
    def __init__(
        self, firstname, lastname, fromEmail, games, onlineHour, nickname, password=None
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.fromEmail = fromEmail
        self.games = games
        self.onlineHour = onlineHour
        self.nickname = nickname

        # creating a random secure password, not informing yet beacause we don't have a login system yet
        self.set_password(password if password else create_strong_password())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)


# oembed_providers = bootstrap_basic(OEmbedCache())
#
# class BlogPost:
#     def __init__(self, nomePost, conteudoPost, descPost, categoriaPost,
#                  imagemPost=None, dataPost=None, aprovado=False):
#         self.nomePost = nomePost
#         self.conteudoPost = conteudoPost
#         self.descPost = descPost
#         self.categoriaPost = categoriaPost
#         self.imagemPost = imagemPost
#         self.dataPost = dataPost if dataPost else datetime.datetime.now()
#         self.aprovado = aprovado
#
#     @property
#     def html_content(self):
#         hilite = CodeHiliteExtension(linenums=False, css_class='highlight')
#         extras = ExtraExtension()
#         markdown_content = markdown(self.conteudoPost, extensions=[hilite, extras])
#         oembed_content = parse_html(
#             markdown_content,
#             oembed_providers,
#             urlize_all=True)
#         return Markup(oembed_content)
