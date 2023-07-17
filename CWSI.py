# Import necessary libraries
import streamlit as st
import openai

# Define a list of assignments
assignments = ["CWSI", "Rebuttal"]  # Add more assignments as needed

# Define main function for the streamlit app
def main():

    st.title("Assignment Feedback")

    # Create a dropdown menu for the assignments
    selected_assignment = st.selectbox("Select an assignment:", options=filtered_assignments)

    # Display the selected assignment
    st.write(f"You selected {selected_assignment}")

    # Create a text input box for the writing sample
    user_input = st.text_area("Enter your text here:", height=200)

    # Access the OpenAI API Key from secrets
    openai_api_key = st.secrets["openai_api_key"]

    # Set the OpenAI API key
    openai.api_key = openai_api_key
    
    # Create a button that when clicked will generate feedback
    if st.button("Get Feedback"):
        # Use OpenAI's API to generate feedback
        model = "text-davinci-003"

        # Choose the prompt based on the selected assignment
        if selected_assignment == "CWSI":
            prompt = f"""
You are this ESL young learner's debate teacher. Write a constructive, supportive and honest feedback report to the learner about their performance on the CWSI argument model writing task.
A CWSI model argument has the following format:
1. Claim - the thesis or main point of the argument. e.g. "Soda drinks should be banned" (this needn't include a reason)
2. Warrant - the reasoning that supports the claim. e.g. "Because, soda drinks are unhealthy"
3. Support - the evidence and/or examples that support the claim. e.g. "For example, the NCBI found that soda contains a lot of sugar which is a known cause of diabetes"
4. Impact - the consequence (why the audience should care). e.g. "This is important because diabetes kills more than 50,000 people per year and substantially reduces quality of life."

Part 1: Friendly and supportive opening
For example, a student who did very well might get a statement like: "Great job! You're doing really well at writing CWSI arguments.". Whereas, a 
student who has significant problems might get a statement like: "Great effort! There's some parts of your CWSI argument that are really good and some parts that could use improvement."

Part 2: Use the following rubric to analyze the student writing (comment on every category):
"1. Is the claim/thesis is a clear statement that can be supported with evidence and facts?
2. Is the warrant/reasoning for the claim clear and logical? Is connective language like 'because' used?
3. Are clear and persuasive evidence or examples are provided that logically support the warrant and claim?
4. Is the impact/consequence of the claim clear and substantial? Ideally, is the impact is quantified?
5. Overall, is the CWSI argument in its entirety written persuasively?
6. Were there any errors in English usage that need correcting?"

Part 3: Provide some suggestions on how to elaborate their argument to make it more persuasive. For example, you could suggest adding additional examples, 
suggest quantifying an impact, using more descriptive or persuasive language, etc. You could also provide modeling for the learner if the have missed a 
part of the argument. If you give a suggestion, try to give them an example of how to do it. 

Finally:
Check your report for consistency, accuracy, and completeness of the steps above. Remember, you are the teacher and you are writing to the student.
Here's the student writing to evaluate:
{user_input}

"""
        elif selected_assignment == "Rebuttal":
            prompt = f"""
You are this ESL young learner's debate teacher. Write a constructive, supportive and honest feedback report to the learner about their performance on the rebuttal writing task.
A rebuttal is an attack on an argument.

Part 1: Friendly and supportive opening
For example, a student who did very well might get a statement like: "Great job! You're doing really well at writing rebuttal.". Whereas, a 
student who has significant problems might get a statement like: "Great effort! There's some parts of your rebuttal that are really good and some parts that could use improvement."

Part 2: Use the following rubric to analyze the student writing (comment on every category):
"1. Is the opponent's argument signposted e.g. "They said/the opponents stated that...?
2. Is a clear counterclaim made that directly attacks the oponent's claim?
3. Is the counterclaim elaborated and supported by logical reasoning?
4. Is the counterclaim suppoorted by relevant evidence and examples?
5. Overall, is the rebuttal in its entirety written persuasively?
6. Were there any errors in English usage that need correcting?"

Part 3: Provide some specific suggestions on how to elaborate their rebuttal to make it more persuasive. For example, you could suggest adding additional examples, 
suggest quantifying evidence, using more descriptive or persuasive language, etc. You could also provide modeling for the learner if the have missed a 
part of the rebuttal. If you give a suggestion, try to give them an example of how to do it. 

Finally:
Check your report for consistency, accuracy, and completeness of the steps above. Remember, you are the teacher and you are writing to the student.
Here's the student writing to evaluate:
{user_input}

"""
        else:
            st.error(f"Invalid assignment: {selected_assignment}")
            return None

        try:
            response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=400, temperature=0.2)
            feedback = response.choices[0].text.strip()
        except Exception as e:
            st.error(f"Error: {e}")
            return None

        # Display the feedback
        st.write(feedback)

# Call the main function
if __name__ == "__main__":
    main()
