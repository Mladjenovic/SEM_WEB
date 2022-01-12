import pandas as pd

course_file = pd.read_csv('courses.csv')

#print(course_file)

#print(course_file.Course)


f = open("course.txt", "w+")


encoded_list = []
course_url = []
course_ects = []
course_goals = []
course_outcomes = []
professors_list = []
professors_url = []
professors_email = []

for course in course_file.Course:
    encoded_list.append(str(course))

for course in course_file.CourseURL:
    course_url.append(str(course))

for course in course_file.CourseECTS:
    course_ects.append(str(course))

for course in course_file.Goals:
    course_goals.append(str(course))

for course in course_file.Outcomes:
    course_outcomes.append(str(course))

for course in course_file.Professors:
    professors_list.append(str(course))

for course in course_file.ProfessorsURL:
    professors_url.append(str(course))

for course in course_file.ProfessorsMail:
    professors_email.append(str(course))

for item in zip(professors_list, professors_url, professors_email):
    for i in item:
        f.write("<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#" + item[1] + "\">\"\n")
        f.write("\t<rdf:type rdf:resource=\"http://www.semanticweb.org/stefan/ontologies/2021/11/sotis-model#Profesor\"/>\n")
        print("Full name: " + str(item[1]))
        f.write("\t<aiiso_sotis:professorFullName>" + item[1] + "</aiiso_sotis:professorFullName>\n")
        print("Mail: " + str(item[2]))
        f.write("\t<aiiso_sotis:professorMail>" + item[2] + "</aiiso_sotis:professorMail>\n")
        print("URL: " + str(item[1]))
        f.write("\t<aiiso_sotis:professorURL>" + item[1] + "</aiiso_sotis:professorURL>\n")
        f.write("</owl:NamedIndividual>\n")
        f.write("\n")
        f.write("\n")
        break
    print("")


"""
for item in zip(course_ects, course_goals, course_outcomes, course_url, encoded_list, professors_url):
    for i in item:
        f.write("<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#" + item[4] + "\">\\n")
        f.write("\t<rdf:type rdf:resource=\"http://www.semanticweb.org/stefan/ontologies/2021/11/sotis-model#Subject\"/>\n")
        print("Contains profesor: " + str(item[5]))
        f.write("\t<contains_professors rdf:resource=\"http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#" + item[5] + "\">\"\n")
        print("SubjectTitle: " + str(item[4]))
        f.write("\t<aiiso_sotis:subjectTitle>" + item[4] + "</aiiso_sotis:subjectTitle>\n")
        print("ECTS: " + str(item[0]))
        f.write("\t<aiiso_sotis:subjectECTS>" + item[0] + "</aiiso_sotis:subjectECTS>\n")
        print("Goal: " + str(item[1]))
        f.write("\t<aiiso_sotis:subjectGoal>" + item[1] + "</aiiso_sotis:subjectGoal>\n")
        print("Outcomes: " + str(item[2]))
        f.write("\t<aiiso_sotis:subjectOutcomes>" + item[2] + "</aiiso_sotis:subjectOutcomes>\n")
        print("URL: " + str(item[3]))
        f.write("\t<aiiso_sotis:subjectURL>" + item[3] + "</aiiso_sotis:subjectURL>\n")
        f.write("</owl:NamedIndividual>\n")
        f.write("\n")
        f.write("\n")
        break
    print("")
"""


"""
for item in encoded_list:
    f.write("<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#" + str(item) + "\">\"\n")
    f.write("\t<rdf:type rdf:resource=\"http://www.semanticweb.org/stefan/ontologies/2021/11/sotis-model#Subject\"/>\n")
    f.write("</owl:NamedIndividual>\n")
    f.write("\n")
    f.write("\n")
"""

"""
    f.write("<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#sotis_professorFullName\">\n")
    f.write("\t<rdf:type rdf:resource=\"http://www.semanticweb.org/stefan/ontologies/2021/11/sotis-model#Profesor\"/>\n")
    f.write("\t<professorFullName>" + str(course) + "</professorFullName>\n").encode('utf-8')
    f.write("</owl:NamedIndividual>\n")
    f.write(" \n")
    f.write(" \n")

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/stefan/ontologies/2021/11/aiiso_sotis#sotis_subject">
        <rdf:type rdf:resource="http://www.semanticweb.org/stefan/ontologies/2021/11/sotis-model#Subject"/>
        <subjectTitle>objektno programiranje</subjectTitle>
    </owl:NamedIndividual>
"""