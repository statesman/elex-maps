import csv, sys, simplejson

# And walk the CSV
def build_race_file(target_race, filename):

  # Get the JSON fil
  fd = open('turnout.geojson', 'r')
  text = fd.read()
  fd.close()
  geo = simplejson.loads(text)

  races = []
  current_precinct = None
  running_vote_total = 0
  precinct_data = {}

  with open('2014results.csv', 'rb') as input_file:

    # Open a reader for the input file
    results = csv.reader(input_file, delimiter=',')
    next(results, None)

    # Loop over the input, parse & write the new file
    for row in results:

      # Pull our data from the CSV columns
      precinct = row[0]
      candidate_name = row[2]
      total_votes = int(row[4])
      race = row[1]
      party = row[3]

      if race == target_race:

        if current_precinct != precinct and current_precinct != None:
          if running_vote_total > 0:
            sorted_races = sorted(races, key=lambda k: k['votes'], reverse=True)
            precinct_data[current_precinct] = {
              'races': sorted_races,
              'winner': sorted_races[0],
              'precinct': current_precinct
            }

          races = []
          running_vote_total = 0

        races.append({
          'candidate': candidate_name,
          'votes': total_votes,
          'party': party
        })

        current_precinct = precinct

        # Keep a running vote total to calculate the percentage down the road
        running_vote_total = running_vote_total + total_votes

  for key, feature in enumerate(geo['features']):
    precinct = feature['properties']['PCT']

    del feature['properties']

    try:
      feature['properties'] = precinct_data[precinct]
    except KeyError:
      pass

  json_out = open('race-data/' + filename + '.json', 'w')
  json_out.write(simplejson.dumps(geo))
  json_out.close()

build_race_file("GOVERNOR", 'governor')
build_race_file("LIEUTENANT GOVERNOR", 'lt-governor')
build_race_file("ATTORNEY GENERAL", 'attorney-general')

build_race_file("MAYOR, CITY OF AUSTIN", 'mayor')
build_race_file("DISTRICT 1, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d1')
build_race_file("DISTRICT 2, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d2')
build_race_file("DISTRICT 3, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d3')
build_race_file("DISTRICT 4, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d4')
build_race_file("DISTRICT 5, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d5')
build_race_file("DISTRICT 6, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d6')
build_race_file("DISTRICT 7, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d7')
build_race_file("DISTRICT 8, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d8')
build_race_file("DISTRICT 9, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d9')
build_race_file("DISTRICT 10, AUSTIN CITY COUNCIL, CITY OF AUSTIN", 'council-d10')

build_race_file("DISTRICT 10, UNITED STATES REPRESENTATIVE", 'us-rep-10')
build_race_file("DISTRICT 17, UNITED STATES REPRESENTATIVE", 'us-rep-17')
build_race_file("DISTRICT 21, UNITED STATES REPRESENTATIVE", 'us-rep-21')
build_race_file("DISTRICT 25, UNITED STATES REPRESENTATIVE", 'us-rep-25')
build_race_file("DISTRICT 35, UNITED STATES REPRESENTATIVE", 'us-rep-35')

build_race_file("DISTRICT 46, STATE REPRESENTATIVE", "state-house-46")
build_race_file("DISTRICT 47, STATE REPRESENTATIVE", "state-house-47")
build_race_file("DISTRICT 48, STATE REPRESENTATIVE", "state-house-48")
build_race_file("DISTRICT 49, STATE REPRESENTATIVE", "state-house-49")
build_race_file("DISTRICT 50, STATE REPRESENTATIVE", "state-house-50")
build_race_file("DISTRICT 51, STATE REPRESENTATIVE", "state-house-51")

build_race_file("DISTRICT 14, STATE SENATOR", "state-senate-14")
build_race_file("DISTRICT 25, STATE SENATOR", "state-senate-25")

build_race_file("UNITED STATES SENATOR", 'senate')