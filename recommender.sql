/*
create function
	textSplitter() returns text[] 
AS $$
begin
select string_to_array(body, ' ')
from legalCases


end
$$
Language SQL;
*/ 

