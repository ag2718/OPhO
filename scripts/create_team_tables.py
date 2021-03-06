from utils import run_async, get_connection

problem_number = 55

async def execute():
    conn = await get_connection()
    team_ids = await conn.fetch('SELECT user_id FROM user_details WHERE user_id > 333')
    
    for team_id in team_ids:
        create_table = f"""
        CREATE TABLE team{team_id[0]}(problem_no integer references problems,solved BOOLEAN NOT NULL, attempts integer, answers decimal[], timestamp timestamp);
        """
        insert_query = f"""
            INSERT INTO team{team_id[0]} (problem_no, solved, attempts) VALUES """ + ', '.join(f"({number}, FALSE, 0)" for number in range(1, problem_number+1)) + ";"
        
        await conn.execute(create_table)
        await conn.execute(insert_query)

run_async(execute())

    