import spacy
import inflect

model = spacy.load('model-best')

def recognize_actor(input):
    nlp_sents = spacy.load("en_core_web_sm")
    nlp_sents.add_pipe("sentencizer")  # Add sentence boundary detection

    p = inflect.engine()
    actors = set()
    usecase = set()
    actors_dict = {}
    current_actor = None
    input = input.lower()
    doc = model(input)

    for ent in doc.ents:
        if ent.label_ == "ACTOR":
            singular_actor = p.singular_noun(ent.text) or ent.text
            actors.add(singular_actor)
        elif ent.label_ == "ACTIVITY":
            usecase.add(ent.text)

    for sent in nlp_sents(input).sents:
        for ent in model(sent.text).ents:
            if ent.label_ == "ACTOR":
                current_actor = p.singular_noun(ent.text) or ent.text
            elif ent.label_ == "ACTIVITY":
                actor_key = current_actor or actors_dict.get(None)
                if actor_key not in actors_dict:
                    actors_dict[actor_key] = set()
                actors_dict[actor_key].add(ent.text)

    return actors_dict

print(recognize_actor('''User and administrator can view profile'''))

















