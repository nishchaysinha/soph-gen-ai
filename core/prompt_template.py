from langchain.prompts import PromptTemplate

def init_prompt(file_structure_list):
    initial_prompt_template = PromptTemplate.from_template(
        """
        The following is the folder structure in the form of a list for a project i am trying to run, 
        
        {file_structure}

        determine the correct commands necessary to execute the project.
        Only give the bash commands necessary to execute the project in the json format below.
        Ensure these are consistent commands that can be run in a bash terminal.
        json format is "bash_commands": ["command_1, command_2, command_3"], "loop_run": true(Always true in first instance to ensure the code runs successfully)
        Make Sure the commands are in the order they want to be executed in.
        NOTE: DO NOT ADD EXPLANATIONS TO THE COMMANDS.
        """
    )


    x = PromptTemplate.format(initial_prompt_template,file_structure=file_structure_list)
    # convert prompt to string

    return x

def generate_prompt(response):
    prompt_template = PromptTemplate.from_template(
        """
        After Executing the last bash commands, the following is the output:

        {response_text}

        Please determine if the code has been run successfully(If yes then loop_run will be set to false) and if not, determine the correct commands necessary to execute the project.
        Only give the bash commands necessary to execute the project in the json format below.
        json format = "bash_commands": "command_1\ncommand_2\ncommand_3", "loop_run": true/false
        Make Sure the commands are in the order they want to be executed in. Ensure that you execute the code.
        
        NOTE: DO NOT ADD EXPLANATIONS TO THE COMMANDS.


        """
    )

    x = PromptTemplate.format(prompt_template, response_text=response)
    return x