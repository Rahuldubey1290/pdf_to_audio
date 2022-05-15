import pyttsx3
import PyPDF2

def main():
    try:
        with open('Presentation1.pdf', 'rb') as pdfFileObj:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
            pages = pdfReader.numPages
            print(f"The total number of pages is :{pages}")
            inp = int(input('Press 1 for single page and 2 for pages and 3 for all pages\n'))

            engine = pyttsx3.init()
            engine.setProperty('rate', 170)

            if inp == 1:
                readPage = int(input('Enter the page you want to read:\n'))
                pageObj = pdfReader.getPage(readPage)
                text = (pageObj.extractText())
                print(text)
                wantListen = (input('Do you want to listen this ?. Yes Or No \n'))
                if 'yes' in wantListen:
                    engine.say(text)
                    engine.runAndWait()

            elif inp == 2:
                givenPage1 = int(input('Enter the starting page number:\n'))
                givenPage2 = int(input('Enter the finishing page number:\n'))
                for page in range(givenPage1, givenPage2 + 1):
                    pageObj = pdfReader.getPage(page)
                    text = (pageObj.extractText())
                    print(text)
                    engine.say(text)
                    engine.runAndWait()

            elif inp == 3:
                for page in range(pages):
                    pageObj = pdfReader.getPage(page)
                    text = (pageObj.extractText())
                    print(text)
                    engine.say(text)
                    engine.runAndWait()



    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
