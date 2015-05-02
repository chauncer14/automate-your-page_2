def generate_concept_HTML(concept_title, concept_description, number_color_alternating):
        if(number_color_alternating % 2 == 0):
            html_text_1 = '''
            <div class="LessonBody">
            <h2>''' + concept_title +"</h2>" 
            html_text_2 = '''
            <div class="concept-description">
            ''' + concept_description

        else:
            html_text_1 = '''
            <div class="LessonBody2">
            <h2>''' + concept_title +"</h2>" 
            html_text_2 = '''
            <div class="concept-description">
            ''' + concept_description

        html_text_3 = '''
            </div>
        </div>'''
        full_html_text = html_text_1 + html_text_2 + html_text_3
        return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    number_color_alternating = concept[2]
    return generate_concept_HTML(concept_title, concept_description, number_color_alternating)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Lesson 4: Introduction to Serious Programming', 'Unlike machines, which are typically physically designed to do a single task, computers are programmable to perform multiple tasks.   Computers can pretty much do anything as long as we can write the sequence of instructions telling them what to do.  We call these sequences of instructions programs. Everything from web browsers to games and mobile apps are simply a precise sequence of steps, that a person wrote using one of the various programming languages for the computer to follow and execute.',1],
                             ['Lesson 5: Variables and Strings', 'Variables let programmers assign names to values, which we can then refer to our programs. This helps programs make more sense for humans, as we can assign names that help us understand what is happening within a program. Variables can change within a program when assigned a new value.',2],
                             ['Lesson 6: Input, functions, and Outputs', 'Functions take in inputs, data that we want to alter in some way, perform an action on that data, creating an output. Functions help programmers avoid repetition because we can define it once and refer to it many times. The return keyword tells Python exactly what the function should produce as output. ',3],
                             ['Lesson 7: Control Flow & Loops: if or else and while', 'Control flows help us execute different code based on certain conditions. If or else are keywords that let us tell what we want to run in different situations. While loop lets us repeat a block of code many times until a certain condition is met. Code under loops is always indented.',4],
                             ['Lesson 8: Debugging', 'Debugging in an important step of writing code. The last line of Python error messages are the best place to start, as it will tell you what line the problem occurs on.',5],
                             ['Lesson 9: Structured Data: Lists & For Loops', 'Lists are one way that we structure data. Lists are helpful because we can then run through all the elements of a list using a for loop.',6],
                             ['Lesson 10: How to Solve Problems', 'Problems can be very complicated, but become much more manageable once broken down in to single functions. The first step in solving large problems is to understand the problem. Next, figure out what are the inputs, and what are the outputs.',7]]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)


