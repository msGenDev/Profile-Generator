#    Profile Generator 0.1 - Developed By Giuseppe Sanfrancesco

#    Follow me
#    Web:     http://www.giuseppesanfrancesco.it
#    GitHub:  https://github.com/Sanfra1407
#    Twitter: https://twitter.com/Sanfra1407
#    Google+: https://plus.google.com/111608398805484520935/


class Profile:
       
    def generateProfile():
        name = input("Insert your name: ")
        surname = input("Insert your surname: ")
        website = input("Insert your website\n(Example: http://google.com): ")
        twitter = input("Insert your Twitter username: ")

        file = open(name.lower() + "-" + surname.lower() + ".html","w")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>About " + name + " " + surname + "</title>\n")
        file.write("<style>" + Profile.makeCSS() + "</style>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<h2>Name: <strong>" + name + "</strong></h2>\n")
        file.write("<h2>Surname: <strong>" + surname + "</strong></h2>\n")
        file.write('<h2>Website: <a href="' + website + '" target="_blank">' + website + "</a></h2>\n")
        file.write('<h2>Twitter: <a href="https://twitter.com/' + twitter + '" target="_blank">' + twitter + "</a></h2>\n")
        file.write("</body>\n")
        file.write("</html>\n")
        file.close()

        print("\n" + name.lower() + "-" + surname.lower() + ".html has been created!")

    def makeCSS():
        css = "\n"
        css += "@import url('http://fonts.googleapis.com/css?family=Open+Sans:400,300,600');\n"
        css += "body{background:url('http://www.giuseppesanfrancesco.it/templates/ja_t3_blank/themes/sito/images/bg-pattern.png')}\n"
        css += "h2{font-weight:normal; font-family:'Open Sans'}\n"
        css += "a{color:royalblue; text-decoration:none; transition:color ease-out 1s;-webkit-transition: color ease-out 1s;}\n"
        css += "a:hover{color:red; transition:color ease-out 1s; -webkit-transition:color ease-out 1s;}"
        css += "\n"
        return css
