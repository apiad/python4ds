import streamlit as st


def title():
    return "Why are we here?"


def run():
    st.write("""
    Welcome! Let's start by knowing each other better.

    My name is Alejandro, I'm a college professor in the Computer Science
    major at the University of Havana. What's your name?
    """)

    name = st.text_input("How do you want me to call you?")

    if not name:
        return

    st.write(f"""
    👋 Hi {name}! Pleased to meet you. 
    
    Now that we know each other, let me try to guess why you're here, and tell you why I'm here.

    ## Why are we here, then?

    Maybe you're here because you heard of this thing called *"Data Science"* and you want
    to learn a bit about it. Or maybe you're here because you are interest in learning how
    to code, and you've heard of this language called *"Python"* and want to learn more about it.
    Or maybe you're just curious about these whole coding deal, and don't know where to start.

    If you're here for any of these reasons, I think you are in the right place. 
    If not, then maybe this experience will still be fruitful for you, so why don't you stick around for a bit?
    Now let me tell why I'm here.

    > ### 👉 I'm here to teach you how to **think and code like a data scientist**.
    
    To do that, I'm gonna teach you some programming fundamentals, using the Python programming language, 
    as well as some practical skills.
    The reasons for choosing Python are multiple, but it all boils down, for me, to the purpose of
    getting you up to be effective at solving real-life data science problems as fast as possible.
    """)

    if not st.button("Tell me more! 🙏"):
        return

    with st.beta_expander("What this is not about"):
        st.write(
        """
        Let me tell you what we are *not* here for: This is not a *general-purpose* programming course. 
        We will not cover everything there is to know about programming. 
        We will not cover all the theory, algorithms, and data structures, nor will we cover all the tools and tricks available in Python.
        And this is not a *software development* course. We will not talk about how to make web or mobile apps,
        or go too deep into software engineering concepts.

        This is not a substitute for these kinds of programming courses, and you definitely should look
        into that in due time if you find it interests you.
        Some of the things I'll teach you will be useful to get you started on those paths.
        But when we're finished, you're not gonna be anywhere near done with learning.
        On the contrary, I expect you'll be so excited that you'll jump at the very next chance you have to keep learning.

        This is a very different kind of experience to any other programming course. 
        We are going to focus very narrowly on the set of concepts and skills you'll need to get started in the world of data science. 
        But this doesn't mean we will cover things superfically. When we need it,
        we will go down the rabbit hole on a particular problem until we understand very well why that something is the way it is.
        However, we will only look at any piece of theory when it's absolutely fundamental to our understanding.
        """)

    with st.beta_expander("What about math?"):
        st.write("""
        Contrary to what some people might have told you, you *don't* need college-level math before getting on the data science train.
        Don't get me wrong, math *is* crucial, but here's a secret: *you can learn it along the way*.
        In this course, I'll introduce any relevant math concept in just as much detail as it is necessary for us to carry on, and no deeper.
        This might leave you wishing to go deeper. If that's the case, then great, I'll give you plenty of links to go on.
        
        Just know that, to begin, only highschool-level math is required, and not even most of it.
        I promise, even if you think you don't know enough math, it's very likely you do.
        Just give us both a chance yo prove it to you.
        """)

    with st.beta_expander("How will this work?"):
        st.write(
        """
        This "course" is structured in a very unique way. Most programming courses start from the fundamental concepts
        and build all the way up, giving you each time more and more complex challenges to solve.
        And that's fine, but that's not what we're gonna do.

        Here, we will focus on building skills, not learning concepts. 
        Concepts will be necessary, and we'll get them as we need them. 
        But we will always have a practical skill as our goal.
        This means that some of the things you'll learn, you'll learn them in a very different way than what most other people do. 
        I ask you to give me the benefit of the doubt, and let me guide you the way I think you will enjoy it the most.

        Another key difference is that we will not distinguish between "reading" and "coding", or "theory" and "practice".
        We will be, *all the time*, learning theory and practicing skills. 
        There are no exercises for later, or questions at the end of a "chapter".
        You will only be able to advance by putting into practice *everything* you learn, every minute of the way.
        """)

    st.write("""
    ## Are you ready to begin? 🚀

    Then go to the sidebar and select "Lesson 1". Let's get started!
    """)
