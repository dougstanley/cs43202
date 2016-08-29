**********************
Systems Administration
**********************

CS 4/53202 Sec 001 Fall 2016
############################

.. footer:: 

   CS 4/53202 Systems Administration Syllabus Fall 2016 - Page: ###Page###

:Instructor: Douglas Stanley
:Email: dmstanle@kent.edu or dostanle@cs.kent.edu
:Website: http://www.cs.kent.edu/~dostanle/courses/cs43202/
:Location: MSB 106
:Time: M-W 9:15 AM - 10:30 AM
:Office Hours: TBD 10:30AM - 11:30 AM or by appointment
:Syllabus: https://github.com/dougstanley/cs43202/
:Version: 1.1
:Modified: 08/29/2016

Course Description:
===================

From the course catalog:
------------------------

    "THE SETTING UP AND DAY-TO-DAY ADMINISTRATION OF
    MULTIUSER MULTITASKING SYSTEMS, SUCH AS THE VARIOUS
    VERSIONS OF UNIX, TOGETHER WITH THE ANALYSIS OF
    PROBLEMS WHICH CAN ARISE IN THESE ACTIVITIES."


Prerequisites:
--------------

CS 33211 Operating Systems


Purpose
=======

To learn the core skills and best practices required to manage modern day
computer systems with a focus on managing unix-like operating systems and the
unix philosophy. This course also serves as a practical look at operating
systems and their role in today's data driven world. Lastly, we will also be
examining the role that systems administration plays in managing the
infrastructure required in today's world of agile development and continuous
software delivery.


Learning Outcomes and Expectations
==================================

After completing this course, you should be able to:

1. Research a problem or task and synthesize information from multiple sources
   to solve the problem or complete the task at hand.

2. Write effective documentation that you or anyone else could use later to
   recreate your end solution, or fix the problem you are documenting.

3. Feel comfortable navigating the command line interface to manipulate the
   system you are managing, including managing files, processes, users, 
   software, system configurations, etc.

4. Utilize SSH and related tools to remotely manage servers and infrastructure.

5. Utilize scripting languages and other automation tools to automate manual
   processes to remove potential human error and improve efficiency.

6. Perform backups and utilize software configuration management tools to be
   able to recreate systems efficiently.

7. Apply security best practices to perform basic server and network
   hardening.

8. Understand the networking protocols and network services that make the
   internet work (TCP/IP, DNS, HTTP, SMTP, etc).

9. Perform system and service health monitoring.



Course Outline:
---------------

+-------+------------------------------------------+------------+
| Week  | Topic                                    | Chapter    |
+=======+==========================================+============+
| 1     | Research and Documentation Writing       |            |
+-------+------------------------------------------+------------+
| 2     | Working the command line                 | 3          |
+-------+------------------------------------------+------------+
| 3-4   | Installing and managing software         | 4          |
+-------+------------------------------------------+------------+
| 5     | Users, groups, processes and permissions | 5          |
+-------+------------------------------------------+------------+
| 6     | Scripting and Intro to Automation        |            |
+-------+------------------------------------------+------------+
| 7     | System services and daemons              | 6 & 8      |
+-------+------------------------------------------+------------+
| 8     | The File System Hierarchy                | 7 & 10     |
+-------+------------------------------------------+------------+
| 9     | Networking                               | 11 & 12    |
+-------+------------------------------------------+------------+
| 10-11 | Local and Network Security               | 13-15 & 22 |
+-------+------------------------------------------+------------+
| 12-13 | Protocols Powering the Internet          | 16-19      |
+-------+------------------------------------------+------------+
| 14    | Containers and Micro Services            |            |
+-------+------------------------------------------+------------+
| 15    | Final Projects                           |            |
+-------+------------------------------------------+------------+


Text:
=====

*Wale Soyinka (2016)*. **Linux Administration: A Beginner's Guide.** *7th ed.*

New York: McGraw-Hill Education [2016]. ISBN: 978-0-07-184537-3


Additional Materials:
---------------------

Additional materials for the course may be found at:
https://github.com/dougstanley/cs43202/


Additional References:
----------------------

* http://docutils.sourceforge.net/docs/user/rst/quickstart.html

* http://docutils.sourceforge.net/docs/user/rst/quickref.html

* http://rst.ninjs.org

* http://daringfireball.net/projects/markdown/basics

* http://daringfireball.net/projects/markdown/syntax

* http://www.ctrlshift.net/project/markdowneditor/

* http://markable.in/editor/

.. raw:: pdf
    
    PageBreak

Grades:
=======

+---------------------------------+----------------+
| Assessment                      | Percentage     |
|                                 | of Final Grade |
+=================================+================+
| Homeworks and Quizzes           | 50%            |
+---------------------------------+----------------+
| Written Midterm Exam            | 10%            |
+---------------------------------+----------------+
| Projects                        | 20%            |
+---------------------------------+----------------+
| Written Final Exam              | 10%            |
+---------------------------------+----------------+
| Final Project                   | 10%            |
+---------------------------------+----------------+
| \*\*Attitude and Attendance     | \*             |
+---------------------------------+----------------+
| **Total Possible Percentage**   | **100%**       |
+---------------------------------+----------------+

.. note:: 

   \* Attitude and attendance points are at the discretion of the
   instructor. **EXCESSIVE ABSENCES AND POOR ATTITUDE WILL AFFECT YOUR FINAL
   GRADE.**

   \*\* **NO LATE HOMEWORK WILL BE ACCEPTED.** When the date for the
   homework and quizzes on Blackboard closes it will not be re-opened. 

   \*\*\* Tests **CANNOT** be made up!



Total points for the course will be calculated and a percentage calculated for
a letter grade.

+--------------+------------+
| Letter Grade | Percentage |
+==============+============+
| A            | 100-93%    |
+--------------+------------+
| A-           | 92-90%     |
+--------------+------------+
| B+           | 89-88%     |
+--------------+------------+
| B            | 87-83%     |
+--------------+------------+
| B-           | 82-80%     |
+--------------+------------+
| C+           | 79-78%     |
+--------------+------------+
| C            | 77-73%     |
+--------------+------------+
| C-           | 72-70%     |
+--------------+------------+
| D+           | 69-68%     |
+--------------+------------+
| D            | 67-63%     |
+--------------+------------+
| D-           | 62-60%     |
+--------------+------------+
| F            | Below 60%  |
+--------------+------------+

Final Exam
==========

*Thursday December 15th 2016* (**12/15/16**) from **10:15am-12:30pm**
in the course classroom **MSB 106**

Student Ethics and Other Policy Information
===========================================

University Policies
-------------------

Enrollment & registration
~~~~~~~~~~~~~~~~~~~~~~~~~

The official registration deadline for this course is **9/4/16**. University
policy requires all students to be officially registered in each class they
are attending. Students who are not officially registered for a course by
published deadlines should not be attending classes and will not receive
credit or a grade for the course. Each student must confirm enrollment by
checking his/her class schedule (using Student Tools in FlashLine) prior to
the deadline indicated. Registration errors must be corrected prior to the
deadline.

.. note:: Students who names do not appear on the University's official class
    roster by the registration deadline, will not be permitted to participate
    (participate in discussions, turn in homework, or receive credit). 


Withdrawal Policy
~~~~~~~~~~~~~~~~~

*Last Day to Drop:* **09/11/16**
*Last Day to Withdraw:* **11/06/16**


Plagiarism and Academic Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

University policy 3-01.8 deals with the problem of academic dishonesty,
cheating, and plagiarism.  None of these will be tolerated in this class.
The sanctions provided in this policy will be used to deal with any
violations.  If you have any questions, please read the policy at
http://www.kent.edu/policyreg/administrative-policy-regarding-student-cheating-and-plagiarism
and/or ask.


Regarding Students with Disabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

University policy 3-01.3 requires that students with disabilities be provided
reasonable accommodations to ensure their equal access to course content. If
you have a documented disability and require accommodations, please contact
the instructor at the beginning of the semester to make arrangements for
necessary classroom adjustments. Please note, you must first verify your
eligibility for these through Student Accessibility Services (contact
330-672-3391 or visit www.kent.edu/sas for more information on registration
procedures).


Course Policies 
----------------

Absences
~~~~~~~~

You may lose attendance points for every absence. If you can't make it to
class for any reason, contact the instructor prior to the class session.
Tests and Labs are to be taken on time. If you are unable to take a test or do
a Lab during the regularly scheduled class time, you must contact the
instructor before the test and have a valid excuse. There are NO make-up tests
or Labs!

Too many consecutively missed classes and assignments will lead to the filing
of a grade of SF (stopped attending Fail). The University wants to know as soon
as possible when a student stops attending. Therefore, if you know you will be
missing classes, please let me know a head of time. Also, a grade of SF can be
changed back to a normal grade, if you resume attending class and turning in
assignments. I will always try to contact you via email several times prior to
turning in a grade of SF as well.


Course Concerns
~~~~~~~~~~~~~~~

If you have any concerns, regarding anything related to the course, please
contact the instructor. 

Deadlines
~~~~~~~~~

It is your responsibility to meet all of the deadlines for every class
session, assignments, and assignment task. Assignments will be given
deadlines--ANY assignments not turned in on the designated due dates and
times, will be considered late and counted as a zero(0) for that assignment.


Ethics
~~~~~~

Students are expected to display ethical behavior at all times. Cheating,
plagiarism, etc., will not be tolerated. The consequences of dishonest
behavior will be commensurate with the activity to include, but not be limited
to, an 'F' for the class, dialogue with administrators, and dismissal from the
college.


Grades
~~~~~~

During the semester, I will track grades by point values of the various
assignments. Letter grades will not be calculated until the end of the
semester, and will use the previously mentioned grade scale.

It is up to you to keep track of your current approximate grade during the
semester, and to see me if you feel there is something wrong. Grades for
assignments will be tracked in blackboard.

Student grades will be submitted to the appropriate department at the end of
the semester (due dates for grades are determined by Kent State University).


Misc
~~~~

**STUDENTS ARE REQUIRED TO FOLLOW ALL LAB, DEPARTMENTAL, COLLEGE, AND
UNIVERSITY RULES AND REGULATIONS AND ALL LAWS.** It is the student's
responsibility to know, understand, and obey these rules, regulations, and
laws. Some of them include:

* All course prerequisites must be met. 

* Only registered students may attend class (no friends or children). 

* No plagiarism. 

.. note:: All cell phones, pagers, and other devices must be set to vibrate or
    turned off during class. The sound on laptop or other computers must be
    turned off during class. Students are expected to not interrupt when
    another person is talking and to not disrupt the class by talking to
    others when someone is presenting.  Students are not to use computers,
    PDAs, etc. for any purpose other than authorized class-related activities
    when class is in session.


.. note:: This Syllabus is subject to change at the instructor's discretion.
    Please check https://github.com/dougstanley/cs43202/ for the
    most recent version.
