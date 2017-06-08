class Py2Pug:
    def __init__(self, doctype='doctype html', indent=2):
        self.html = Html()
            self.doctype = doctype
            self.indent = indent
	
	def compileToPug(self):
		pass

class Html:
    def __init__(self):
        self.head = Head()
        self.body = Body()


class Head:
    def __init__(self):
        self.content = Tag('head')

        def addContent(self, content):
            pass


class Body:
    def __init__(self):
        self.content = Tag('body')

        def addContent(self, content):
            pass


class Tag:
    def __init__(self, tagName, classNames=None, idName=None, attributes=None, content=None):
        self.tagName = tagName
        self.classNames = classNames
        self.idName = idName
        self.attributes = attributes
        self.content = content

        def compileClassNames(self):
            if self.classNames not None:
                return ''.join(['.{}'.format(className) for className in self.classNames])
            else:
                return None

        def compileAttributes(self):
            if self.attributes not None:
                return '({})'.format(' '.join(self.attributes))
            else:
                return None

        def addContent(self, content):
            pass

        def __str__(self):
            return '''{tagName}{classNames}{idName}{attributes}{content}'''.format(self.tagName, self.classNames, self.idName, self.attributes, self.content)


pug = Py2Pug()
pug.html.head.addContent(Tag('script'))
pug.html.body.addContent(Tag('div', classNames=['ts', 'btn', 'primary'], idName='button', attributes=['@click="doSth()"', ':value=""'], content=Tag('p'))
                         )
pug.compileToPug()