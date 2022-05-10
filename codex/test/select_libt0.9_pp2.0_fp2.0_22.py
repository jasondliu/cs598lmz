import selectTutorialByTag
import selectEmailDistinct


def createTutorial(image, name, topic, duration, description, isPublic,
	tagList, fileName):

	# Generate a dict that will hold all info about tutorial

	tutorialDict = {}

	tutorialDict['image'] = str(image)
	tutorialDict['name'] = str(name)
	tutorialDict['topic'] = str(topic)
	tutorialDict['duration'] = str(duration)
	tutorialDict['description'] = str(description)
	tutorialDict['isPublic'] = str(isPublic)

	# Storing tag id and tag name in tag list

	for tag in tagList:

		if selectTagByName.selectTagByName(tag[1]) == 'Not Found':

			# Call add tag function to add tag and get tag id

			tagId = 1
			tag[0] = tagId

			tagList = [tag]
			tutorialDict['tag'] = tagList

