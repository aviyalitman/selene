from update_seqweaver import UpdateSeqweaver
import sys

if __name__ == "__main__":

    input_path = '/r04/al6117/CureGN/CLIP_data/human.hg19.peaks.sorted.bed.gz'
    train_path = '/r04/al6117/CureGN/CLIP_data/training_data/train.h5'
    validate_path = '/r04/al6117/CureGN/CLIP_data/training_data/valid.h5'
    feature_path = '/r04/al6117/CureGN/CLIP_data/data.hg19.colnames'
    hg19_fasta = '/r04/al6117/CureGN/CLIP_data/hg19.fa'
    yaml = '/r04/al6117/CureGN/selene/selene_sdk/train_seqweaver.yml'

    print("loading data object...")
    # testing object initiation and attributes
    data = UpdateSeqweaver(input_path, train_path, validate_path, feature_path, hg19_fasta, yaml)
    #print(old_data.sequence_len)
    #print(old_data.feature_set)

    # testing training data construction
    #print("constructing training data...")
    #data.construct_training_data()
    #print("done.")
    print("training model...")
    print(data.train_model())
    print("done.")
