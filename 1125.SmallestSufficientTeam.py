'''
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.
Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.
For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.
It is guaranteed an answer exists.
Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
'''
from functools import cache

class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        m=len(req_skills)
        n=len(people)
        skill_index={v:i for i,v in enumerate(req_skills)}
        cand=[]
        for skills in people:
            val=0
            for skill in skills:
                val |=1<<skill_index[skill]

            cand.append(val)

        @cache
        def fn(i,mask):
            if mask==0:
                return []

            if i==n:
                return [0]*100

            if not (mask & cand[i]):
                return fn(i+1,mask)

            return min(fn(i+1,mask),[i]+fn(i+1,mask &~cand[i]),key=len)

        return fn(0,(1<<m)-1)