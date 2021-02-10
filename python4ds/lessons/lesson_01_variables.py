import streamlit as st


def title():
    return "What is data?"


def run():
    st.write("""
    Any process in data science starts with data.

    You can think of data as a collection of facts, each one can be as simple or as complicated as you want.
    The smallest unit of data that's useful is probably a single number:

    ```python
    31
    ```

    But this number is useless unless we assign some meaning to it.
    Is it someone's age? Is it a price? Is it the number of days since something happened?

    The easiest way to assign it some meaning is by giving this number *a name* that *means something to us*.

    ```python
    my_age = 31
    ```

    > (This is my real age, though, at least when I started writing this... 😝)

    In Python, we give names to things by using **variables**. A variable is just a name that *refers* to something.
    And that name can be *anything* that you want. It's your responsibility to give things names that are meaningful for you,
    or anyone else, that comes back later to read your code.

    The way we say, in Python, that a variable refers to something (like a number) is how you just saw, by simply writing `variable = something`.

    So, let's try that. Tell my what's your age, in Python code, the way I just did before.
    """)

    your_age_expression = st.text_input("Tell me your age in Python code")

    if not your_age_expression:
        return
    
    global_vars = {}

    try:
        exec(your_age_expression, global_vars)
        your_age = global_vars['my_age']
        assert isinstance(your_age, int)
        assert your_age > 0
    except SyntaxError:
        st.error("🙃 That code doesn't seem right. Make sure you typed everything as I taught you.")
        return
    except KeyError:
        st.error("🙃 That code doesn't tell me your age. Make sure your variable is called `my_age`, the way I did before.")
        return
    except AssertionError:
        st.error("🙃 That code doesn't seem right. Your age should be a whole number, greater than 0.")
        return

    if your_age == 31:
        st.warning("🤔 Are you sure that's your real age? You didn't copied and pasted *my* code, right? Ok, I'll believe you...")

    if your_age < 10 or your_age > 90:
        st.warning("🤔 Are you sure that's your real age? It seems a bit... extreme. Ok, I'll believe you...")

    st.success("🥳 There you go! You just wrote your first program in Python!")

    st.write("""
    > ### 🏆 You have discovered a Fundamental Concept: **naming things**.

    > In a computer program, we always give names to everything: values, operations, even specific fragments of code.
    By naming things conveniently, we make sure *everyone* knows what our program is *meant* to do.
    We'll be seeing this concept over a over as we learn more.
    """)

    st.write(f"""
        ## What about "real" numbers?

        In order to express most of the interesting facts precisely, we need more that whole numbers.
        For example, your very own age almost surely is not exactly {your_age}, but something between
        {your_age} and {your_age + 1}, right?

        In math, we have the *integer numbers*, which are just whole numbers, and the *real numbers*, which are 
        those with decimal values (you might know there are more sets of numbers, but let's stick to the basics).
        Maybe you'll remember the mathematical symbols that represent all the integer and real numbers: $\mathcal{{N}}$
        and $\mathcal{{R}}$ respectively.

        In a computer, we cannot really represent *whatever* real number we want, for a very simple reason: your RAM memory is finite.
        So, for example, $\pi = 3.14159265...$ is a number with an infinite non-periodic decimal expansion (that's just a fancy
        way of saying it goes on an on after the dot).
        So instead we have the next best thing, an approximation of the real numbers that has a significant number
        of limitations. We will talk about many of those limitations as they become relevant but, for now, just keep
        in mind that there are some numbers (actually, a lot of them) that you cannot represent precisely in a computer program,
        because your RAM memory is limited.

        As you might (or not) expect, numbers with decimal values are written with a dot (`.`) separating the whole
        part from the decimal part:

        ```python
        pi = 3.14159265 # (not really, only approximately)
        ```

        > By the way, that piece of gray text starting with `#` is what we call a *comment*. You can put these
        anywhere in your program and they are completely ignored by the computer. There are useful to leave, well, comments
        to other programmers (or yourself).
    """)

    st.write("""
        ## What about letters?

        Numbers are far from the only type of data we need to express facts.
        The second most basic type of is probably text, which is funny, because it's both super simple and
        also capable of expressing the most complex concepts, right?

        In Python, we denote a piece of literal text between pairs of `"`, like this.
        They can be as long as you want, and have any letter, including spaces, smileys, 
        and anything you can write on a text message, basically.

        ```python
        my_name = "Alejandro Piad"
        ```

        Go on, give it a try:
    """)

    your_name_expression = st.text_input("Tell me your name in Python code")

    if not your_name_expression:
        return
    
    global_vars = {}

    try:
        exec(your_name_expression, global_vars)
        your_name = global_vars['my_name']
        assert isinstance(your_name, str)
    except SyntaxError:
        st.error("🙃 That code doesn't seem right. Make sure you typed everything as I taught you.")
        return
    except KeyError:
        st.error("🙃 That code doesn't tell me your age. Make sure your variable is called `my_name`, the way I did before.")
        return
    except NameError:
        st.error("🙃 That code doesn't seem right. Make sure your enclosing your name in a pair of `\"` like I did before.")
        return
    except AssertionError:
        st.error("🙃 That code doesn't seem right. Your name should be a non-empty literal text, between pairs of `\"`.")
        return

    if your_name == "Alejandro Piad":
        st.warning("🤔 Are you sure that's your real name? You didn't copied and pasted *my* code, right? Ok, I'll believe you...")

    st.success(f"🥳 Congrats, **{your_name}**, with age **{your_age}**. Now you know three types of data!")

    st.write("""
        You can go a long way with just text and numbers. Actually, we could argue that everything, in the end,
        is just a *composition* of numbers and text.
    """)

    st.info("""
        📝 Technically speaking, whole numbers in Python (and most programming languages) are called `integers`
        (just like their mathematical name), while decimal numbers are called `floats` 
        (which stands for *floating-point*, something we'll explain later),
        and fragments of text are called `strings`, for historical purposes (they are strings of letters 🤷).
        So now you know, when others mention these funny names, they're just talking about numbers and text. 
        
        👉 We'll stick to their technical name from now on,
        just to be fancy 😉.
    """)

    st.write("""
        ## ⚠️ The type of the data matters!

        Now that you know two, well, techincally three, different types of data, it's important to get rid
        of a common source of mistakes. You can represent apparently the same datum with all three, 
        but they are actually different, and that difference matters.

        If you say `a = 25` as opposed to `a = 25.0`, *mathematically* you're saying
        the same things, but *computationally* these are two different values.
        The reason is because these are values of two different *types* (integers and floats) and
        you should *always* be clear of the exact type you're dealing with.
    """)